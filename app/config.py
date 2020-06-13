import os

basedir = os.path.abspath(os.path.dirname(__file__))
CONTOUR = os.environ.get('CONTOUR', 'testing')
if CONTOUR == 'testing':
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
else:
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
AUTH_URI = 'http://' + os.environ.get('AUTH_URI', '127.0.0.1') + ":" + os.environ.get('AUTH_PORT', '5001')
WTF_CSRF_ENABLED = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'SECRET'
MSG_QUEUE = os.environ.get('MSG_QUEUE')
UPLOAD_FOLDER = "/csv/"
if not os.path.exists(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)


STANDART_PAGE_COUNT = 20
