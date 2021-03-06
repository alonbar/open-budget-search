import elasticsearch
import logging
import re
from datetime import date
from types_data import TYPES_DATA

INDEX_NAME = 'obudget'
logger = logging.getLogger('obudget')
hdlr = logging.FileHandler('obudget.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.WARNING)

ES_SERVERS_LIST = ['127.0.0.1']
DEFAULT_TIMEOUT = 60
EXEMPTION_SERACH_FIELD_LIST = ["exemptions.publisher", "exemptions.regulation", "exemptions.supplier", "exemptions.contact", "exemptions.contact_email", "exemptions.description", "exemptions.reason", "exemptions.decision", "exemptions.url", "exemptions.subjects", "exemptions.source_currency", "exemptions.page_title", "exemptions.entity_kind"]
BUEDGET_SERACH_FIELD_LIST = ["budget.title","budget.req_title", "budget.change_title", "budget.change_type_name", "budget.budget_title", "budget.pending", "budget.properties"]
# OLDEST_DATE = "0000-00-00"
# DEFAULT_SIZE = 3


def get_es_client():
    return elasticsearch.Elasticsearch(ES_SERVERS_LIST, timeout=DEFAULT_TIMEOUT)


def search(term):
    es = get_es_client()
    return simple_search_exemptions(es, term)


def index_doc(type_name, doc):
    es = get_es_client()
    return es.index(index=INDEX_NAME, doc_type=type_name, body=doc)

def get_type_definition(type):
    for definition in TYPES_DATA:
        if definition["type_name"] == type:
            return definition

def preperare_typed_query(type,term, from_date, to_date, search_size, offset):
      type_definition = get_type_definition(type)
      body= {
                "query": {
                    "filtered": {
                        "query": {
                            "query_string": {
                                "fields": type_definition["search_fields"],
                                "query": term
                            }
                        }
                    }
                },
              "aggs": {
                  "stats_per_month":{
                      "date_histogram":{
                          "field": type_definition["type_name"] + "." + type_definition['date_fields']['from'],
                          "interval": "month"
                     }
                },
                "filtered": {
                  "filter": {
                    "bool": {
                      "must": [
                        {
                          "type": {
                            "value": type
                          }
                        },
                        {
                          "range": type_definition['range_structure']
                        }
                      ]
                    }
                  },
                "aggs": {
                    "top_results": {
                        "top_hits": {
                            "size": int(search_size),
                            "from": int(offset),
                            "highlight" : {
                                "fields": {
                                    "*": {}
                                }
                            },
                            "sort": type_definition['sort_method']

                        }
                    }
                }
            }
          },
          "size": 0
        }

      range_obj = body["aggs"]["filtered"]["filter"]["bool"]["must"][1]["range"]
      if type == "exepmtion":
          range_obj[type_definition['date_fields']['from']]["gte"] = from_date
          range_obj[type_definition['date_fields']['to']]["lte"] = to_date
      else:
          range_obj[type_definition['date_fields']['from']]["gte"] = from_date
          range_obj[type_definition['date_fields']['to']]["lte"] = to_date


      print(body)
      return body


def parse_highlights(highlights):
    start_tag = '<em>'
    end_tag = '</em>'
    parsed_highlights = {}
    for field in highlights:
        parsed_highlights[field] = []
        for term in highlights[field]:
            start_tag_results = re.finditer(start_tag, term)
            end_tag_results = re.finditer(end_tag, term)
            for start, end in zip(start_tag_results,end_tag_results):
                    result_index = start.end() - len(start_tag)
                    result_len = end.start() - start.end()
                    parsed_highlights[field].append([result_index, result_len])

    return parsed_highlights

def parse_budget_result(elastic_result):
    buget_result = {}
    buget_result["current"]
    buget_result["past"]
    buget_result["total"] = elastic_result["aggregations"]["filtered"]["top_results"]["hits"]["hits"]
    for i, doc in enumerate(elastic_result["aggregations"]["filtered"]["top_results"]["hits"]["hits"]):
                    buget_result[type]["docs"][i] = {}
                    buget_result[type]["docs"][i]["source"] = doc["_source"]
                    buget_result[type]["docs"][i]["highlight"] = parse_highlights(doc["highlight"])




def search(types, term, from_date, to_date, size, offset):
    es = get_es_client()
    elastic_result = {}
    ret_val = {}
    for type in types:
        query_body = preperare_typed_query(type, term,from_date, to_date, size, offset)
        elastic_result[type] = es.search(index="obudget", body=query_body)
        ret_val[type] = {}

        ret_val[type]["total_in_time_range"] = len(elastic_result[type]["aggregations"]["filtered"]["top_results"]["hits"]["hits"])
        ret_val[type]["total_overall"] = elastic_result[type]["hits"]["total"]
        ret_val[type]["docs"] = {}
        ret_val[type]["data_time_distribution"] = elastic_result[type]["aggregations"]["stats_per_month"]["buckets"]
        for i, doc in enumerate(elastic_result[type]["aggregations"]["filtered"]["top_results"]["hits"]["hits"]):
            ret_val[type]["docs"][i] = {}
            ret_val[type]["docs"][i]["source"] = doc["_source"]
            ret_val[type]["docs"][i]["highlight"] = parse_highlights(doc["highlight"])


    return ret_val


def simple_search_exemptions(a,b):
    return True
