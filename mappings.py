EXEMPTIONS_MAPPING = {
        'properties': {
            'publication_id': {
                'type': 'integer'
            },
            'publisher': {
                'type': 'string',
                'analyzer': 'hebrew'
            },
            'regulation': {
                'type': 'string',
                'analyzer': 'hebrew'
            },
            'supplier': {
                'type': 'string',
                'analyzer': 'hebrew'
            },
            'supplier_id': {
                'type': 'long'
            },
            'start_date': {
                'type': 'date',
                'format': 'date'
            },
            'end_date': {
                'type': 'date',
                'format': 'date'
            },
            'claim_date': {
                'type': 'date',
                'format': 'date'
            },
            'last_update_date': {
                'type': 'date',
                'format': 'date'
            },
            'contact': {
                'type': 'string',
                'analyzer': 'hebrew'
            },
            'contact_email': {
                'type': 'string',
                'index': 'not_analyzed'
            },
            'description': {
                'type': 'string',
                'analyzer': 'hebrew'
            },
            'volume': {
                'type': 'long'
            },
            'reason': {
                'type': 'string',
                'analyzer': 'hebrew'
            },
            'decision': {
                'type': 'string',
                'analyzer': 'hebrew'
            },
            'url': {
                'type': 'string',
                'index': 'not_analyzed'
            },
            'subjects': {
                'type': 'string',
                'analyzer': 'hebrew'
            },
            'source_currency': {
                'type': 'string',
                'index': 'not_analyzed'
            },
            'page_title': {
                'type': 'string',
                'analyzer': 'hebrew'
            },
            'entity_id': {
                'type': 'long'
            },
            'entity_kind': {
                'type': 'string',
                'index': 'not_analyzed'
            }
        }
    }


BUDGET_MAPPING = {
        'properties': {
            'code': {
                'type': 'string'
            },
            'year': {
                'type': 'integer'
            },
            'title': {
                'type': 'string',
                'analyzer': 'hebrew'
            },
            'net_allocated': {
                'type': 'long'
            },
            'net_revised': {
                'type': 'long'
            },
            'net_used': {
               'type': 'long'
            },
            'gross_allocated': {
               'type': 'long'
            },
            'gross_revised': {
               'type': 'long'
            },
            'personnel_allocated': {
               'type': 'long'
            },
            'personnel_revised': {
               'type': 'long'
            },
            'commitment_allocated': {
               'type': 'long'
            },
            'commitment_revised': {
               'type': 'long'
            },
            'amounts_allocated': {
               'type': 'long'
            },
            'amounts_revised': {
               'type': 'long'
            },
            'contractors_allocated': {
               'type': 'long'
            },
            'contractors_revised': {
               'type': 'long'
            },
            'dedicated_allocated': {
               'type': 'long'
            },
            'dedicated_revised': {
               'type': 'long'
            },
            'contractors_allocated': {
               'type': 'long'
            },
            'contractors_allocated': {
               'type': 'long'
            },
            'contractors_allocated': {
               'type': 'long'
            },
            'contractors_allocated': {
               'type': 'long'
            },
            'contractors_allocated': {
               'type': 'long'
            },
            'equiv_code': {
                'type': 'string',
                'analyzer': 'hebrew'
            },
            'group_full': {
                'type': 'string',
                'analyzer': 'hebrew'
            },
            'group_top': {
                'type': 'string',
                'analyzer': 'hebrew'
            },
            'class_full': {
                'type': 'string',
                'analyzer': 'hebrew'
            },
            'group_top': {
                'type': 'string',
                'analyzer': 'hebrew'
            },
            'class_top': {
                'type': 'string',
                'analyzer': 'hebrew'
            },
            'kind': {
                'type': 'string',
                'analyzer': 'hebrew'
            },
            'subkind': {
                'type': 'string',
                'analyzer': 'hebrew'
            }
        }
    }


SUPPORT_MAPPING = {
        'properties': {
            'year': {
                'type': 'long'
            },
            'subject': {
                'type': 'string',
                'analyzer': 'hebrew'
            },
            'code': {
                'type': 'string'
            },
            'recipient': {
                'type': 'string',
                'analyzer': 'hebrew'
            },
            'kind': {
                'type': 'string',
                'analyzer': 'hebrew'
            },
            'title': {
                'type': 'string',
                'analyzer': 'hebrew'
            },
            'num_used': {
                'type': 'long'
            },
            'amount_allocated': {
                'type': 'long'
            },
            'entity_id': {
                'type': 'string'
            },
            'entity_kind': {
                'type': 'string'
            }
        }
    }

CHANGES_MAPPING = {
        'properties': {
            'year': {
                'type': 'long'
            },
            'leading_item': {
                'type': 'long'
            },
            'req_code': {
                'type': 'long'
            },
            'req_title': {
                'type': 'string',
                'analyzer': 'hebrew'
            },
            'change_code': {
                'type': 'long'
            },
            'change_title': {
                'type': 'string',
                'analyzer': 'hebrew'
            },
            'change_type_id': {
                'type': 'long'
            },
            'change_type_name': {
                'type': 'string',
                'analyzer': 'hebrew'
            },
            'committee_id': {
                'type': 'long'
            },
            'budget_code': {
                'type': 'string'
            },
            'budget_title': {
                'type': 'string',
                'analyzer': 'hebrew'
            },
            'net_expense_diff': {
                'type': 'long'
            },
            'gross_expense_diff	': {
                'type': 'long'
            },
            'allocated_income_diff': {
                'type': 'long'
            },
            'commitment_limit_diff	': {
                'type': 'long'
            },
            'personnel_max_diff': {
                'type': 'long'
            },
            'date': {
                'type': 'date',
                'format': 'date'
            },
            'pending': {
                'type': 'string',
                'analyzer': 'hebrew'
            },
            'equiv_code': {
                'type': 'string',
                'analyzer': 'hebrew'
            }
        }
    }


CHANGES_MAPPING = {
        'properties': {
            'model': {
                'type': 'string'
            },
            'selector': {
                'type': 'string'
            },
            'time': {
                'type': 'date',
                'format': 'date'
            },
            'req_title': {
                'type': 'string',
                'analyzer': 'hebrew'
            },
            'change_code': {
                'type': 'long'
            },
            'change_title': {
                'type': 'string',
                'analyzer': 'hebrew'
            },
            'change_type_id': {
                'type': 'long'
            },
            'change_type_name': {
                'type': 'string',
                'analyzer': 'hebrew'
            },
            'committee_id': {
                'type': 'long'
            },
            'budget_code': {
                'type': 'string'
            },
            'budget_title': {
                'type': 'string',
                'analyzer': 'hebrew'
            },
            'net_expense_diff': {
                'type': 'long'
            },
            'gross_expense_diff	': {
                'type': 'long'
            },
            'allocated_income_diff': {
                'type': 'long'
            },
            'commitment_limit_diff	': {
                'type': 'long'
            },
            'personnel_max_diff': {
                'type': 'long'
            },
            'date': {
                'type': 'string'
            },
            'pending': {
                'type': 'string',
                'analyzer': 'hebrew'
            },
            'equiv_code': {
                'type': 'string',
                'analyzer': 'hebrew'
            }
        }
    }

CHANGE_HISTORY_MAPPING = {
        'properties': {
            'year': {
                'type': 'long'
            },
            'subject': {
                'type': 'string',
                'analyzer': 'hebrew'
            },
            'code': {
                'type': 'string'
            },
            'recipient': {
                'type': 'string',
                'analyzer': 'hebrew'
            },
            'kind': {
                'type': 'string',
                'analyzer': 'hebrew'
            },
            'title': {
                'type': 'string',
                'analyzer': 'hebrew'
            },
            'num_used': {
                'type': 'long'
            },
            'amount_allocated': {
                'type': 'long'
            },
            'entity_id': {
                'type': 'string'
            },
            'entity_kind': {
                'type': 'string'
            }
        }
    }