from flask import request
from flask_api import status

from auth.requests import check_token_is_authenticated, check_token_is_authenticated_admin
from views.answers import unauthorised, notAdmin


def check_auth(func):
    def wrapper():
        if 'access_token' in request.headers and check_token_is_authenticated(request.headers['access_token']):
            return func()
        else:
            return unauthorised(), status.HTTP_401_UNAUTHORIZED

    wrapper.__name__ = func.__name__
    return wrapper

def check_admin(func):
    def wrapper():
        if 'access_token' in request.headers and check_token_is_authenticated_admin(request.headers['access_token']):
            return func()
        else:
            return notAdmin(), status.HTTP_401_UNAUTHORIZED

    wrapper.__name__ = func.__name__
    return wrapper