from flask import jsonify, request, current_app
from flask_api import status

from db_data.User import isAuthenticated, isAuthenticatedUser, isAuthenticatedAdmin


@current_app.route('/is_authenticated', methods=['GET'])
def is_authenticated():
    if 'access_token' in request.headers and isAuthenticated(request.headers['access_token']):
        return jsonify(result=1), status.HTTP_200_OK
    return jsonify(result=0), status.HTTP_200_OK


@current_app.route('/is_authenticated_user', methods=['GET'])
def is_authenticated_user():
    if 'access_token' in request.headers and isAuthenticatedUser(request.headers['access_token']):
        return jsonify(result=1), status.HTTP_200_OK
    return jsonify(result=0), status.HTTP_200_OK

@current_app.route('/is_authenticated_admin', methods=['GET'])
def is_authenticated_admin():
    if 'access_token' in request.headers and isAuthenticatedAdmin(request.headers['access_token']):
        return jsonify(result=1), status.HTTP_200_OK
    return jsonify(result=0), status.HTTP_200_OK