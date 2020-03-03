from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.config import SQLALCHEMY_DATABASE_URI

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app.view import *

if __name__ == '__main__':
    app.run(debug=True)
