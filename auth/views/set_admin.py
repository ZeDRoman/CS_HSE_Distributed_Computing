from flask import request, current_app, g
from flask_api import status

from db_data.User import  isAuthenticatedAdmin, getUser
from views.answers import success, noSuchUser, accesEmailNotProvided, notAdmin


@current_app.route('/set_admin', methods=['GET', 'POST'])
def set_admin():
    if 'access_token' in request.headers and 'email' in request.headers:
        email = request.headers['email']
        access_token = request.headers['access_token']
        if isAuthenticatedAdmin(access_token):
            user = getUser(email=email)
            if user:
                user.set_admin()
                return success(), status.HTTP_200_OK
            else:
                return noSuchUser(), status.HTTP_400_BAD_REQUEST
        return notAdmin(), status.HTTP_400_BAD_REQUEST
    return accesEmailNotProvided(), status.HTTP_400_BAD_REQUEST

@current_app.route('/downgrade', methods=['GET', 'POST'])
def downgrade():
    if 'access_token' in request.headers and 'email' in request.headers:
        email = request.headers['email']
        access_token = request.headers['access_token']
        if isAuthenticatedAdmin(access_token):
            user = getUser(email=email)
            if user:
                user.set_user()
                return success(), status.HTTP_200_OK
            else:
                return noSuchUser(), status.HTTP_400_BAD_REQUEST
        return notAdmin(), status.HTTP_400_BAD_REQUEST
    return accesEmailNotProvided(), status.HTTP_400_BAD_REQUEST