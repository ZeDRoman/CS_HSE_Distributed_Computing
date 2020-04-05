from flask_api import status
from flask import request, jsonify

from processing.db_utils import getProductById
from processing.utils import checkIsNumber
from run import app
from views.answers import idNotNumber, idDoesntExists, idNotProvided


@app.route('/product', methods=['get'])
def show_product():
    product_id = request.args.get('id', None)
    if product_id is None:
        return idNotProvided(), status.HTTP_400_BAD_REQUEST

    if not checkIsNumber(product_id, 'product_id'):
        return idNotNumber(), status.HTTP_400_BAD_REQUEST

    product = getProductById(product_id)
    if product is None:
        return idDoesntExists(product_id), status.HTTP_200_OK
    return jsonify(data=product.__repr__()), status.HTTP_200_OK
