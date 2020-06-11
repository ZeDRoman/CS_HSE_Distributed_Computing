import os

basedir = os.path.abspath(os.path.dirname(__file__))
CONTOUR = os.environ.get('contour', 'testing')
if CONTOUR == 'testing':
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
else:
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
MSG_QUEUE = os.environ.get('MSG_QUEUE')
WTF_CSRF_ENABLED = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'SECRET'
CONFIRM_SECRET = os.environ.get('CONFIRM_SECRET', 'secret_token')
CONFIRM_URL = 'http://' + os.environ.get('AUTH_URI', '127.0.0.1') + ":" + os.environ.get('AUTH_PORT', '5001') + "/confirm"