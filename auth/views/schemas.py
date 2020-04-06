authenticate_schema = {
    'type': 'object',
    'properties': {
        'access_token': {'type': 'string'}
    },
    'required': ['access_token']
}


log_in_schema = {
    'type': 'object',
    'properties': {
        'email': {'type': 'string'},
        'password': {'type': 'string'}
    },
    'required': ['email', 'password']
}


refresh_token_schema = {
    'type': 'object',
    'properties': {
        'refresh_token': {'type': 'string'}
    },
    'required': ['refresh_token']
}