from flask_api import status
from flask import request, jsonify, current_app

from auth.auth_wrapper import check_auth
from db_data.Product import Product
from processing.db_utils import getPageAmount, getProducts
from processing.utils import checkIsNumber
from config import STANDART_PAGE_COUNT
from views.answers import pageNotNumber, pageCountNotNumber


@current_app.route('/products', methods=['get'])
@check_auth
def list_products():
    page = request.args.get('page', 1)
    if checkIsNumber(page, 'page'):
        page = max(int(page) - 1, 0)
    else:
        return pageNotNumber(), status.HTTP_400_BAD_REQUEST

    page_count = request.args.get('page_size', STANDART_PAGE_COUNT)
    if checkIsNumber(page_count, 'page_size'):
        page_count = int(page_count)
    else:
        return pageCountNotNumber(), status.HTTP_400_BAD_REQUEST
    page_amount = getPageAmount(page_count, Product.id)
    data = getProducts(page, page_count)
    return jsonify(data=data, page=page + 1, page_amount=page_amount), status.HTTP_200_OK