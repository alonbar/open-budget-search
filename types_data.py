TYPES_DATA = [
    {
        'type_name': 'exemption',
        'mapping': {
            'properties': {
                'publication_id': {
                    'type': 'integer'
                },
                'publisher': {
                    'type': 'string',
                    'analyzer': 'hebrew',
                    'fields': {
                        'raw': {
                            'type': 'string',
                            'index': 'not_analyzed'
                        }
                    }
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
                    'type': 'string'
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
                },
                'subjects': {
                    'type': 'string',
                    'analyzer': 'hebrew'
                },
                'source_currency': {
                    'type': 'string',

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

                }
            }
        }
    },
    {
        'type_name': 'budget',
        'mapping': {
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
    },
    {
        'type_name': 'support',
        'mapping': {
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
    },
    {
        'type_name': 'changes',
        'mapping': {
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
    },
    {
        'type_name': 'change_history',
        'mapping': {
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
    }
]
