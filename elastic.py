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
    create_mapping(CHANGES_TYPE, mappings.CHNAGES_MAPPING)


def initialize_db():
    tables = [SUPPORTS_TYPE, BUDGET_TYPE, EXEMPTIONS_TYPE]
    clean()
    create_index()
    map_tables()
    load_tables('C:/dev/open-budget-search/data', tables)


def search_exemption(term):
    es = get_es_client()
    return es.search(index="obudget", body={"query": {"query_string": {"query": term}}})


if __name__ == "__main__":
    initialize_db();
