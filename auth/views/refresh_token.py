from flask import request, jsonify, current_app
from flask_api import status

from db_data.User import refreshToken
from views.answers import tokenIsRotten, refreshTokenNotProvided

@current_app.route('/refresh_token', methods=['GET', 'POST'])
def refresh_token():
    if 'refresh_token' in request.headers:
        result = refreshToken(request.headers['refresh_token'])
        if result:
            access_token, refresh_token = result
            return jsonify(access_token=access_token, refresh_token=refresh_token), status.HTTP_200_OK
        else:
            return tokenIsRotten(), status.HTTP_401_UNAUTHORIZED
    else:
        return refreshTokenNotProvided(), status.HTTP_401_UNAUTHORIZED