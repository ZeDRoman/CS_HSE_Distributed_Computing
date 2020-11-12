from flask_expects_json import expects_json
from flask import request, current_app
from flask_api import status

from db_data.User import createUserFromJson
from views.answers import success, emailTaken
from views.schemas import log_in_schema


@current_app.route('/register', methods=['GET', 'POST'])
@expects_json(log_in_schema)
def register():
    if createUserFromJson(request.json):
        return success(), status.HTTP_201_CREATED
    else:
        return emailTaken(), status.HTTP_400_BAD_REQUEST