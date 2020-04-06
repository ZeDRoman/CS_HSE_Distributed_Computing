from flask_expects_json import expects_json
from flask import request, jsonify, current_app
from flask_api import status

from db_data.User import refreshToken
from views.answers import tokenIsRotten, refreshTokenNotProvided
from views.schemas import refresh_token_schema

@current_app.route('/refresh_token', methods=['GET', 'POST'])
@expects_json(refresh_token_schema)
def refresh_token():
    if 'refresh_token' in request.headers:
        result = refreshToken(request.json['refresh_token'])
        if result:
            access_token, refresh_token = result
            return jsonify(access_token=access_token, refresh_token=refresh_token), status.HTTP_200_OK
        else:
            return tokenIsRotten(), status.HTTP_401_UNAUTHORIZED
    else:
        return refreshTokenNotProvided(), status.HTTP_401_UNAUTHORIZED