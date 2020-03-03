from flask_api import status

from app import app, db
from app.forms.ProductForm import ProductForm
from app.processing.debug_messages import *
from app.processing.answers import *
from app.processing.utils import formIsValid, checkIsNumber
from app.processing.db_utils import getProductById, getProducts, changeProduct, createProductFromForm
from app.config import *


@app.route('/product/create', methods=['post'])
def create_product():
    product_id = request.form.get('id')
    if not checkIsNumber(product_id, 'product_id'):
        return idNotNumber(), status.HTTP_400_BAD_REQUEST

    form = ProductForm(request.form)
    if not formIsValid(form):
        return str(form.errors), status.HTTP_400_BAD_REQUEST

    if not createProductFromForm(form):
        return idExists(), status.HTTP_400_BAD_REQUEST

    return productCreated(), status.HTTP_201_CREATED


@app.route('/product/delete', methods=['post'])
def delete_product():
    product_id = request.args.get('id')
    if not checkIsNumber(product_id, 'product_id'):
        return idNotNumber(), status.HTTP_400_BAD_REQUEST

    product = getProductById(product_id)
    if product is None:
        return idDoesntExists(product_id), status.HTTP_200_OK
    else:
        db.session.delete(product)
        db.session.commit()

    return productDeleted(), status.HTTP_200_OK


@app.route('/product/edit', methods=['post'])
def edit_product():
    if not checkIsNumber(request.form.get('id'), 'product_id'):
        return idNotNumber(), status.HTTP_400_BAD_REQUEST

    form = ProductForm(request.form)
    if not formIsValid(form):
        return str(form.errors), status.HTTP_400_BAD_REQUEST

    product = getProductById(form.id.data)
    if product is None:
        return idDoesntExists(form.id.data), status.HTTP_200_OK

    changeProduct(product, form.name.data, form.category.data)
    return productEdited(), status.HTTP_200_OK


@app.route('/product', methods=['get'])
def show_product():
    product_id = request.args.get('id')

    if not checkIsNumber(product_id, 'product_id'):
        return idNotNumber(), status.HTTP_400_BAD_REQUEST

    product = getProductById(product_id)
    if product is None:
        return idDoesntExists(product_id), status.HTTP_200_OK
    return product.__repr__(), status.HTTP_200_OK


@app.route('/products', methods=['get'])
def list_products():
    page = request.args.get('page', 0)
    if checkIsNumber(page, 'page'):
        page = int(page)
    else:
        return pageNotNumber(), status.HTTP_400_BAD_REQUEST

    page_count = request.args.get('page_count', STANDART_PAGE_COUNT)
    if checkIsNumber(page_count, 'page_count'):
        page_count = int(page_count)
    else:
        return pageCountNotNumber(), status.HTTP_400_BAD_REQUEST

    return getProducts(page, page_count), status.HTTP_200_OK
