 #!/usr/bin/env python
 # -*- coding: utf-8 -*

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import SQLALCHEMY_DATABASE_URI


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

db.create_all()

from view import *

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
