from flask import request
from flask_api import status

from auth.requests import check_token_is_authenticated
from views.answers import unauthorised


def check_auth(func):
    def wrapper():
        if 'access_token' in request.headers and check_token_is_authenticated(request.headers['access_token']):
            return func()
        else:
            return unauthorised(), status.HTTP_401_UNAUTHORIZED
    return wrapper