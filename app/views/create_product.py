from flask_api import status
from flask_expects_json import expects_json
from flask import request, current_app

from auth.auth_wrapper import check_auth, check_admin
from db_data.Product import productFromJson
from processing.db_utils import createProduct
from views.answers import success
from views.schemas import create_product_schema


@current_app.route('/product', methods=['put'])
@expects_json(create_product_schema)
@check_admin
def create_product():
    product = productFromJson(request.json)
    createProduct(product)
    return success(), status.HTTP_201_CREATED