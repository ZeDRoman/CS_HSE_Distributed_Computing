from flask_api import status
from flask_expects_json import expects_json
from flask import request

from run import app
from db_data.Product import productFromJson
from processing.db_utils import createProduct
from views.answers import success
from views.schemas import create_product_schema


@app.route('/product', methods=['put'])
@expects_json(create_product_schema)
def create_product():
    product = productFromJson(request.json)
    createProduct(product)
    return success(), status.HTTP_201_CREATED