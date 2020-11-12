import os
from _csv import reader
from flask_api import status

from flask import request, current_app
from db_data.Product import Product
from processing.db_utils import createProduct
from processing.utils import send_confirmation_csv_file
from views.answers import success, fileNotProvided, fileIsNotAllowed
import time


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in "csv"


def secure_filename():
    return str(int(time.time())) + ".csv"


@current_app.route('/csv', methods=['GET', 'POST'])
def load_csv():
    if request.method == 'POST':
        file = request.files['file']
        if not file:
            return fileNotProvided(), status.HTTP_400_BAD_REQUEST
        if not allowed_file(file.filename):
            return fileIsNotAllowed(), status.HTTP_400_BAD_REQUEST
        filename = secure_filename()
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        send_confirmation_csv_file(filename)
        import logging
        logging.warning(os.listdir(current_app.config['UPLOAD_FOLDER']))
        return success(), status.HTTP_201_CREATED