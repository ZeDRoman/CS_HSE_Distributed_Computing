from flask import g

# from run import db
from db_data.Product import Product

db = g.db


def getProductById(product_id):
    product = db.session.query(Product).filter(Product.id == product_id).first()
    if product:
        return product
    else:
        return None


def deleteProduct(product):
    db.session.delete(product)
    db.session.commit()


def getProducts(page, page_count):
    first = (page) * page_count
    last = (page + 1) * page_count
    objs = db.session.query(Product).slice(first, last)
    return list(map(Product.__repr__, objs))


def changeProduct(product, new_name, new_category):
    product.name = new_name
    product.category = new_category
    db.session.commit()


def createProduct(product):
    db.session.add(product)
    db.session.commit()
    return True


def getPageAmount(pageSize, column):
    amount = db.session.query(db.func.count(column)).scalar()
    return (amount + pageSize - 1) // pageSize