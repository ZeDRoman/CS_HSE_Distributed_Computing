from flask_expects_json import expects_json
from flask import request, jsonify, current_app
from flask_api import status
import jwt

from config import CONFIRM_SECRET
from db_data.User import confirm_user
from views.answers import invalidConfirmToken, success


@current_app.route('/confirm', methods=['GET', 'POST'])
def confirm():
    confirm_token = request.args.get('confirm_token', None)
    data = jwt.decode(confirm_token, CONFIRM_SECRET)
    if "email" not in data or "password" not in data or len(data) != 2 or \
            not confirm_user(data["email"], data["password"]):
        return invalidConfirmToken(), status.HTTP_400_BAD_REQUEST

    return success(), status.HTTP_200_OK