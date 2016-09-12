import elasticsearch
import logging

INDEX_NAME = 'obudget'
logger = logging.getLogger('obudget')
hdlr = logging.FileHandler('obudget.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.WARNING)

ES_SERVERS_LIST = ['127.0.0.1']
DEFAULT_TIMEOUT = 60
EXEMPTIONS_FIELDS_LIST = ["publisher", "regulation", "supplier", "contact", "contact_email", "description", "reason", "decision", "url", "subjects", "source_currency", "page_title", "entity_kind"]
# OLDEST_DATE = "0000-00-00"
# DEFAULT_SIZE = 3

def get_es_client():
    return elasticsearch.Elasticsearch(ES_SERVERS_LIST, timeout=DEFAULT_TIMEOUT)

def search(term):
    es = get_es_client()
    return simple_search_exemptions(es, term)


def prepare_exemption_query(term, fields, start_date, end_date, search_size, offset):
    body={
          "from": offset,
          "size": search_size,
          "query": {
            "filtered": {
              "query": {
                 "query_string": {
                    "fields": fields,
                    "query": term
                 }
              },
              "filter": {
                "type": { "value" : "exemptions"}
              },
                "filter": {
                  "range": {
                    "start_date": {
                        "gte": start_date
                    },
                    "end_date": {
                        "lte": end_date
                    }
                }
              }
            }
          },
        "sort": [
            { "start_date":   { "order": "desc" , "ignore_unmapped" : True}},
            { "volume": { "order": "desc", "ignore_unmapped" : True }}
        ]
        }
    return body


def search_exemptions(term, filters, start_date, end_date, offset, size):
    es = get_es_client()
    fields = EXEMPTIONS_FIELDS_LIST
    if filters != "NULL":
        fields = []
        for field in str(filters).split(','):
            fields.append(field)
    elastic_result = es.search(index="obudget", body=prepare_exemption_query(term, fields, start_date, end_date, size, offset))
    ret_val = {}
    if elastic_result["hits"]["total"] > 0:
        ret_val["total"] = elastic_result["hits"]["total"]
        ret_val["hits"] = elastic_result["hits"]["hits"]
    else:
        ret_val["total"] = 0
    return ret_val


def simple_search_exemptions(a,b):
    return True
