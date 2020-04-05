from flask_api import status
from flask_expects_json import expects_json
from flask import request

from processing.db_utils import getProductById, deleteProduct
from run import app
from processing.utils import checkIsNumber
from views.answers import success, idNotNumber, idDoesntExists
from views.schemas import delete_product_schema


@app.route('/product', methods=['delete'])
@expects_json(delete_product_schema)
def delete_product():
    product_id = request.json['id']
    if not checkIsNumber(product_id, 'product_id'):
        return idNotNumber(), status.HTTP_400_BAD_REQUEST

    product = getProductById(product_id)
    if product is None:
        return idDoesntExists(product_id), status.HTTP_200_OK
    else:
        deleteProduct(product)
    return success(), status.HTTP_200_OK