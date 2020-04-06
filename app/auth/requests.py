import requests

from config import AUTH_URI


def check_token_is_authenticated(access_token):
    response = requests.get(AUTH_URI + '/is_authenticated',
                            headers={'access_token': access_token}
                            )
    if response and response.json()['result']:
        return True
    return False
