from flask_api import status
from flask_expects_json import expects_json

from run import app
from db_data.Product import productFromJson, Product
from processing.debug_messages import *
from processing.answers import *
from processing.utils import checkIsNumber
from processing.db_utils import getProductById, getProducts, changeProduct, createProduct, \
    getPageAmount, deleteProduct
from config import *

create_schema = {
    'type': 'object',
    'properties': {
        'name': {'type': 'string'},
        'category': {'type': 'string'}
    },
    'required': ['name', 'category']
}


@app.route('/product', methods=['put'])
@expects_json(create_schema)
def create_product():
    product = productFromJson(request.json)
    createProduct(product)

    return success(), status.HTTP_201_CREATED


delete_schema = {
    'type': 'object',
    'properties': {
        'id': {'type': 'integer'}
    },
    'required': ['id']
}


@app.route('/product', methods=['delete'])
@expects_json(delete_schema)
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


edit_schema = {
    'type': 'object',
    'properties': {
        'id': {'type': 'integer'},
        'name': {'type': 'string'},
        'category': {'type': 'string'}
    },
    'required': ['id', 'name', 'category']
}


@app.route('/product', methods=['post'])
@expects_json(edit_schema)
def edit_product():
    product_id = request.json['id']
    if not checkIsNumber(product_id, 'product_id'):
        return idNotNumber(), status.HTTP_400_BAD_REQUEST

    product = getProductById(product_id)
    if product is None:
        return idDoesntExists(product_id), status.HTTP_200_OK

    changeProduct(product, request.json['name'], request.json['category'])
    return success(), status.HTTP_200_OK


show_one_schema = {
    'type': 'object',
    'properties': {
        'id': {'type': 'integer'}
    },
    'required': ['id']
}


@app.route('/product', methods=['get'])
@expects_json(show_one_schema)
def show_product():
    product_id = request.json['id']

    if not checkIsNumber(product_id, 'product_id'):
        return idNotNumber(), status.HTTP_400_BAD_REQUEST

    product = getProductById(product_id)
    if product is None:
        return idDoesntExists(product_id), status.HTTP_200_OK
    return jsonify(data=product.__repr__()), status.HTTP_200_OK


show_schema = {
    'type': 'object',
    'properties': {
        'page': {'type': 'integer'},
        'page_count': {'type': 'integer'}
    }
}


@app.route('/products', methods=['get'])
@expects_json(show_schema)
def list_products():
    page = request.json.get('page', 1)
    if checkIsNumber(page, 'page'):
        page = max(int(page) - 1, 0)
    else:
        return pageNotNumber(), status.HTTP_400_BAD_REQUEST

    page_count = request.json.get('page_count', STANDART_PAGE_COUNT)
    if checkIsNumber(page_count, 'page_count'):
        page_count = int(page_count)
    else:
        return pageCountNotNumber(), status.HTTP_400_BAD_REQUEST
    page_amount = getPageAmount(page_count, Product.id)
    data = getProducts(page, page_count)
    return jsonify(data=data, page=page + 1, page_amount=page_amount), status.HTTP_200_OK

