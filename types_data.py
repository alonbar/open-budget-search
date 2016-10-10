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
                    'analyzer': 'hebrew',
                    'fields': {
                        'raw': {
                            'type': 'string',
                            'index': 'not_analyzed'
                        }
                    }
                },
                'supplier': {
                    'type': 'string',
                    'analyzer': 'hebrew',
                    'fields': {
                        'raw': {
                            'type': 'string',
                            'index': 'not_analyzed'
                        }
                    }
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
                    'analyzer': 'hebrew',
                    'fields': {
                        'raw': {
                            'type': 'string',
                            'index': 'not_analyzed'
                        }
                    }
                },
                'contact_email': {
                    'type': 'string',
                    'fields': {
                        'raw': {
                            'type': 'string',
                            'index': 'not_analyzed'
                        }
                    }
                },
                'description': {
                    'type': 'string',
                    'analyzer': 'hebrew',
                    'fields': {
                        'raw': {
                            'type': 'string',
                            'index': 'not_analyzed'
                        }
                    }
                },
                'volume': {
                    'type': 'long'
                },
                'reason': {
                    'type': 'string',
                    'analyzer': 'hebrew',
                    'fields': {
                        'raw': {
                            'type': 'string',
                            'index': 'not_analyzed'
                        }
                    }
                },
                'decision': {
                    'type': 'string',
                    'analyzer': 'hebrew',
                    'fields': {
                        'raw': {
                            'type': 'string',
                            'index': 'not_analyzed'
                        }
                    }
                },
                'url': {
                    'type': 'string',
                    'fields': {
                        'raw': {
                            'type': 'string',
                            'index': 'not_analyzed'
                        }
                    }
                },
                'subjects': {
                    'type': 'string',
                    'analyzer': 'hebrew',
                    'fields': {
                        'raw': {
                            'type': 'string',
                            'index': 'not_analyzed'
                        }
                    }
                },
                'source_currency': {
                    'type': 'string',
                    'fields': {
                        'raw': {
                            'type': 'string',
                            'index': 'not_analyzed'
                        }
                    }
                },
                'page_title': {
                    'type': 'string',
                    'analyzer': 'hebrew',
                    'fields': {
                        'raw': {
                            'type': 'string',
                            'index': 'not_analyzed'
                        }
                    }
                },
                'entity_id': {
                    'type': 'long'
                },
                'entity_kind': {
                    'type': 'string',
                    'fields': {
                        'raw': {
                            'type': 'string',
                            'index': 'not_analyzed'
                        }
                    }
                }
            }
        },
        'search_fields': ["exemption.publisher", "exemption.regulation", "exemption.supplier", "exemption.contact", "exemption.contact_email", "exemption.description", "exemption.reason", "exemption.decision", "exemption.url", "exemption.subjects", "exemption.source_currency", "exemption.page_title", "exemption.entity_kind"],
        'date_fields': {
            'from' : 'start_date',
            'to': 'end_date'
        },
        'sort_method':[
                        {
                            "start_date": {
                                "order": "desc"
                            }
                        },
                        {
                            "volume": {
                                "order": "desc"
                            }
                        }
                    ]

    },
    {
        'type_name': 'budget',
        'mapping': {
            'properties': {
                'code': {
                    'type': 'string',
                    'fields': {
                        'raw': {
                            'type': 'string',
                            'index': 'not_analyzed'
                        }
                    }
                },
                'year': {
                    'type': 'date'
                },
                'title': {
                    'type': 'string',
                    'analyzer': 'hebrew',
                    'fields': {
                        'raw': {
                            'type': 'string',
                            'index': 'not_analyzed'
                        }
                    }
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
                    'analyzer': 'hebrew',
                    'fields': {
                        'raw': {
                            'type': 'string',
                            'index': 'not_analyzed'
                        }
                    }
                },
                'group_top': {
                    'type': 'string',
                    'analyzer': 'hebrew',
                    'fields': {
                        'raw': {
                            'type': 'string',
                            'index': 'not_analyzed'
                        }
                    }
                },
                'class_full': {
                    'type': 'string',
                    'analyzer': 'hebrew',
                    'fields': {
                        'raw': {
                            'type': 'string',
                            'index': 'not_analyzed'
                        }
                    }
                },
                'group_top': {
                    'type': 'string',
                    'analyzer': 'hebrew',
                    'fields': {
                        'raw': {
                            'type': 'string',
                            'index': 'not_analyzed'
                        }
                    }
                },
                'class_top': {
                    'type': 'string',
                    'analyzer': 'hebrew',
                    'fields': {
                        'raw': {
                            'type': 'string',
                            'index': 'not_analyzed'
                        }
                    }
                },
                'kind': {
                    'type': 'string',
                    'analyzer': 'hebrew',
                    'fields': {
                        'raw': {
                            'type': 'string',
                            'index': 'not_analyzed'
                        }
                    }
                },
                'subkind': {
                    'type': 'string',
                    'analyzer': 'hebrew',
                    'fields': {
                        'raw': {
                            'type': 'string',
                            'index': 'not_analyzed'
                        }
                    }
                }
            }
        },
        'search_fields': ["budget.title","budget.req_title", "budget.change_title", "budget.change_type_name", "budget.budget_title", "budget.pending", "budget.properties"],
        'date_fields': {
            'from': 'from_year',
            'to': 'to_year'
        },
        'sort_method':[
                        {
                            "year": {
                                "order": "desc"
                            }
                        },
                        {
                            "net_revised": {
                                "order": "desc"
                            }
                        }
                    ]
    },
    {
        'type_name': 'supports',
        'mapping': {
            'properties': {
                'year': {
                    'type': 'long'
                },
                'subject': {
                    'type': 'string',
                    'analyzer': 'hebrew',
                    'fields': {
                        'raw': {
                            'type': 'string',
                            'index': 'not_analyzed'
                        }
                    }
                },
                'code': {
                    'type': 'string'
                },
                'recipient': {
                    'type': 'string',
                    'analyzer': 'hebrew',
                    'fields': {
                        'raw': {
                            'type': 'string',
                            'index': 'not_analyzed'
                        }
                    }
                },
                'kind': {
                    'type': 'string',
                    'analyzer': 'hebrew',
                    'fields': {
                        'raw': {
                            'type': 'string',
                            'index': 'not_analyzed'
                        }
                    }
                },
                'title': {
                    'type': 'string',
                    'analyzer': 'hebrew',
                    'fields': {
                        'raw': {
                            'type': 'string',
                            'index': 'not_analyzed'
                        }
                    }
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
                    'type': 'string',
                    'fields': {
                        'raw': {
                            'type': 'string',
                            'index': 'not_analyzed'
                        }
                    }
                }
            }
        }
    },
    {
        'type_name': 'changes',
        'mapping': {
            'properties': {
                'model': {
                    'type': 'string',
                    'fields': {
                        'raw': {
                            'type': 'string',
                            'index': 'not_analyzed'
                        }
                    }
                },
                'selector': {
                    'type': 'string',
                    'fields': {
                        'raw': {
                            'type': 'string',
                            'index': 'not_analyzed'
                        }
                    }
                },
                'time': {
                    'type': 'date',
                    'format': 'date'
                },
                'req_title': {
                    'type': 'string',
                    'analyzer': 'hebrew',
                    'fields': {
                        'raw': {
                            'type': 'string',
                            'index': 'not_analyzed'
                        }
                    }
                },
                'change_code': {
                    'type': 'long'
                },
                'change_title': {
                    'type': 'string',
                    'analyzer': 'hebrew',
                    'fields': {
                        'raw': {
                            'type': 'string',
                            'index': 'not_analyzed'
                        }
                    }
                },
                'change_type_id': {
                    'type': 'long'
                },
                'change_type_name': {
                    'type': 'string',
                    'analyzer': 'hebrew',
                    'fields': {
                        'raw': {
                            'type': 'string',
                            'index': 'not_analyzed'
                        }
                    }
                },
                'committee_id': {
                    'type': 'long'
                },
                'budget_code': {
                    'type': 'string'
                },
                'budget_title': {
                    'type': 'string',
                    'analyzer': 'hebrew',
                    'fields': {
                        'raw': {
                            'type': 'string',
                            'index': 'not_analyzed'
                        }
                    }
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
                    'analyzer': 'hebrew',
                    'fields': {
                        'raw': {
                            'type': 'string',
                            'index': 'not_analyzed'
                        }
                    }
                },
                'equiv_code': {
                    'type': 'string',
                    'analyzer': 'hebrew',
                    'fields': {
                        'raw': {
                            'type': 'string',
                            'index': 'not_analyzed'
                        }
                    }
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
                    'analyzer': 'hebrew',
                    'fields': {
                        'raw': {
                            'type': 'string',
                            'index': 'not_analyzed'
                        }
                    }
                },
                'code': {
                    'type': 'string'
                },
                'recipient': {
                    'type': 'string',
                    'analyzer': 'hebrew',
                    'fields': {
                        'raw': {
                            'type': 'string',
                            'index': 'not_analyzed'
                        }
                    }
                },
                'kind': {
                    'type': 'string',
                    'analyzer': 'hebrew',
                    'fields': {
                        'raw': {
                            'type': 'string',
                            'index': 'not_analyzed'
                        }
                    }
                },
                'title': {
                    'type': 'string',
                    'analyzer': 'hebrew',
                    'fields': {
                        'raw': {
                            'type': 'string',
                            'index': 'not_analyzed'
                        }
                    }
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
                    'type': 'string',
                    'fields': {
                        'raw': {
                            'type': 'string',
                            'index': 'not_analyzed'
                        }
                    }
                }
            }
        }
    }
]
