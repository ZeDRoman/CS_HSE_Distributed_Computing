from sqlalchemy.exc import IntegrityError

from app.__init__ import app, db
from app.processing.debug_messages import production_form_data, log_db_error
from app.db_data.Product import Product, productFromForm


def getProductById(product_id):
    product = db.session.query(Product).filter(Product.id == product_id).first()
    if product:
        return product
    else:
        return None


def getProducts(page, page_count):
    first = (page - 1) * page_count
    last = page * page_count
    objs = db.session.query(Product).slice(first, last)
    return "\n".join(map(Product.__repr__, objs))


def changeProduct(product, new_name, new_category):
    product.name = new_name
    product.category = new_category
    db.session.commit()


def createProductFromForm(form):
    product = productFromForm(form)

    try:
        db.session.add(product)
        db.session.commit()
    except IntegrityError as ex:
        db.session.rollback()
        app.logger.info(log_db_error(production_form_data(), ex.orig.args))
        return False
    return True
