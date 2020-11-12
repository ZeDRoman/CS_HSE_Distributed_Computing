import os

basedir = os.path.abspath(os.path.dirname(__file__))
CONTOUR = os.environ.get('contour', 'testing')
if CONTOUR == 'testing':
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
else:
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
AUTH_URI = 'http://' + os.environ.get('AUTH_URI', '127.0.0.1') + ":" + os.environ.get('AUTH_PORT', '5001')
WTF_CSRF_ENABLED = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'SECRET'



STANDART_PAGE_COUNT = 20
