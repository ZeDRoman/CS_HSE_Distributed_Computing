 #!/usr/bin/env python
 # -*- coding: utf-8 -*

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from view import *

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
