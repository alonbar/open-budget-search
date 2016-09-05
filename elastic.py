import elasticsearch
import csv
import os
import mappings

ES_SERVERS_LIST = ['127.0.0.1']
DEFAULT_TIMEOUT = 60

INDEX_NAME = 'obudget'
EXEMPTIONS_TYPE = 'exemptions'
BUDGET_TYPE = 'budget'
SUPPORTS_TYPE = 'supports'
CHANGES_TYPE = 'changes'
EXEMPTIONS_FIELDS_LIST = ["publisher", "regulation", "supplier", "contact", "contact_email", "description", "reason", "decision", "url", "subjects", "source_currency", "page_title", "entity_kind"]
OLDEST_DATE = "0000-00-00"
DEFAULT_SIZE = 3

def get_es_client():
    return elasticsearch.Elasticsearch(ES_SERVERS_LIST, timeout=DEFAULT_TIMEOUT)

def clean():
    es = get_es_client()
    if es.indices.exists(INDEX_NAME):
        es.indices.delete(INDEX_NAME)


def create_index():
    es = get_es_client()
    es.indices.create(INDEX_NAME, {
        'settings': {
            'index': {
                'number_of_shards': 6,
                'number_of_replicas': 1
            }
        }
    })


def create_mapping(type,doc_body):
    es = get_es_client()
    es.indices.put_mapping(index=INDEX_NAME, doc_type=type, body=doc_body)


def load_tables(tables_path, tables_list):
    #assuming table name and table type is the same- should change ?
    for table in tables_list:
        load_data(os.path.join(tables_path, table + ".csv"), table)


def load_data(input_path, type):
    es = get_es_client()
    try:
        with open(input_path, 'r', encoding="utf8") as input_file:
            csv_reader = csv.reader(input_file)
            # Parse headers.
            fields_list = []
            headers = next(csv_reader)
            for header in headers:
                fields_list.append(header.lower())
            for idx, row in enumerate(csv_reader):
                document = {}
                for cell, field_name in zip(row, fields_list):
                    cell = cell.strip()
                    if cell:
                        document[field_name] = cell
                try:
                    if idx % 100 == 0:
                        print (idx)
                    es.index(INDEX_NAME, type, document)
                except:
                    print("tried indexing the following doc:")
                    print(document)

    except:
        print ("shit")


def map_tables():
    create_mapping(EXEMPTIONS_TYPE, mappings.EXEMPTIONS_MAPPING)
    create_mapping(BUDGET_TYPE, mappings.BUDGET_MAPPING)
    create_mapping(SUPPORTS_TYPE, mappings.SUPPORT_MAPPING)
    create_mapping(CHANGES_TYPE, mappings.CHANGES_MAPPING)


def initialize_db():
    tables = [EXEMPTIONS_TYPE, BUDGET_TYPE]
    clean()
    create_index()
    map_tables()
    load_tables('C:/dev/open-budget-search/data', tables)


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


def simple_search_exemptions(es, term, query):
    elastic_result =  es.search(index="obudget", body={
                                              "query": {
                                                "filtered": {
                                                  "query": {
                                                     "query_string": {
                                                         "fields": ["publisher", "regulation", "supplier", "contact", "contact_email", "description", "reason", "decision", "url", "subjects", "source_currency", "page_title", "entity_kind"],
                                                        "query": term
                                                     }
                                                  },
                                                  "filter": {
                                                    "type": { "value" : "exemptions"}
                                                  }
                                                }
                                              }
                                            })


if __name__ == "__main__":
    initialize_db();
