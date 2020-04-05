create_product_schema = {
    'type': 'object',
    'properties': {
        'name': {'type': 'string'},
        'category': {'type': 'string'}
    },
    'required': ['name', 'category']
}


delete_product_schema = {
    'type': 'object',
    'properties': {
        'id': {'type': 'integer'}
    },
    'required': ['id']
}


edit_product_schema = {
    'type': 'object',
    'properties': {
        'id': {'type': 'integer'},
        'name': {'type': 'string'},
        'category': {'type': 'string'}
    },
    'required': ['id', 'name', 'category']
}