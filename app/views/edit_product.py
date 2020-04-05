from flask_api import status
from flask_expects_json import expects_json
from flask import request, current_app

from processing.db_utils import getProductById, changeProduct
from processing.utils import checkIsNumber
from views.answers import idNotNumber, idDoesntExists, success
from views.schemas import edit_product_schema


@current_app.route('/product', methods=['post'])
@expects_json(edit_product_schema)
def edit_product():
    product_id = request.json['id']
    if not checkIsNumber(product_id, 'product_id'):
        return idNotNumber(), status.HTTP_400_BAD_REQUEST

    product = getProductById(product_id)
    if product is None:
        return idDoesntExists(product_id), status.HTTP_200_OK

    changeProduct(product, request.json['name'], request.json['category'])
    return success(), status.HTTP_200_OK