from flask_expects_json import expects_json
from flask import request, current_app
from flask_api import status

from db_data.User import logoutUser
from views.answers import success
from views.schemas import refresh_token_schema


@current_app.route('/logout')
@expects_json(refresh_token_schema)
def log_out():
    if 'refresh_token' in request.headers:
        logoutUser(request.headers['refresh_token'])
    return success(), status.HTTP_200_OK