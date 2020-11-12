from flask import jsonify, request, current_app
from flask_api import status

from db_data.User import isAuthenticated


@current_app.route('/is_authenticated', methods=['GET'])
def is_authenticated():
    if 'access_token' in request.headers and isAuthenticated(request.headers['access_token']):
        return jsonify(result=1), status.HTTP_200_OK
    return jsonify(result=0), status.HTTP_200_OK