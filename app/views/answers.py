from flask import jsonify


def idDoesntExists(product_id):
    return jsonify(error=F"Object with id = {product_id} doesnt exist")


def idNotNumber():
    return jsonify(error="Id must be number")


def pageNotNumber():
    return jsonify(error="Page must be number")


def pageCountNotNumber():
    return jsonify(error="Page count must be number")


def idNotProvided():
    return jsonify(error="Id is not provided")


def productCreated():
    return jsonify(error="Product is created")


def productEdited():
    return jsonify(error="Product is edited")


def productDeleted():
    return jsonify(error="Product is deleted")


def success():
    return jsonify(error="Success")
