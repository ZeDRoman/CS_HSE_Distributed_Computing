from flask_expects_json import expects_json
from flask import request, jsonify, current_app
from flask_api import status

from db_data.User import getUser
from views.answers import invalidLogining
from views.schemas import log_in_schema


@current_app.route('/login', methods=['GET', 'POST'])
@expects_json(log_in_schema)
def log_in():
    user = getUser(email=request.json['email'])
    if user is None or not user.check_password(request.json['password']):
        return invalidLogining(), status.HTTP_400_BAD_REQUEST
    access_token, refresh_token = user.log_in()
    return jsonify(access_token=access_token, refresh_token=refresh_token), status.HTTP_200_OK
