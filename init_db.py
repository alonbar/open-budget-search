import json

from elastic import get_es_client, logger
from mappings import EXEMPTIONS_MAPPING, BUDGET_MAPPING, SUPPORT_MAPPING, CHANGES_MAPPING
import os
import csv

INDEX_NAME = 'obudget'
EXEMPTIONS_TYPE = 'exemptions'
BUDGET_TYPE = 'budget'
SUPPORTS_TYPE = 'supports'
CHANGES_TYPE = 'changes'


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


def load_data(input_path, input_type):
    es = get_es_client()
    with open(input_path, 'r', encoding="utf-8") as input_file:
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
            if idx % 100 == 0:
                print(idx)
            try:
                es.index(INDEX_NAME, input_type, document)
            except Exception as e:
                logger.exception("Error indexing INDEX_NAME: %s, input_type: %s, document: %s" % (INDEX_NAME, input_type, json.dumps(document)))


def map_tables():
    create_mapping(EXEMPTIONS_TYPE, EXEMPTIONS_MAPPING)
    create_mapping(BUDGET_TYPE, BUDGET_MAPPING)
    create_mapping(SUPPORTS_TYPE, SUPPORT_MAPPING)
    create_mapping(CHANGES_TYPE, CHANGES_MAPPING)


def initialize_db():
    tables = [EXEMPTIONS_TYPE, BUDGET_TYPE]
    clean()
    create_index()
    map_tables()
    load_tables('data', tables)


if __name__ == "__main__":
    initialize_db()
