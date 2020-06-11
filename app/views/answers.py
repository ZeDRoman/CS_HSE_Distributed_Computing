from flask import jsonify


def idDoesntExists(product_id):
    return jsonify(result="Error", error=F"Object with id = {product_id} doesnt exist")


def idNotNumber():
    return jsonify(result="Error", error="Id must be number")


def pageNotNumber():
    return jsonify(result="Error", error="Page must be number")


def pageCountNotNumber():
    return jsonify(result="Error", error="Page count must be number")


def idNotProvided():
    return jsonify(result="Error", error="Id is not provided")


def productCreated():
    return jsonify(result="Error", error="Product is created")


def productEdited():
    return jsonify(result="Error", error="Product is edited")


def productDeleted():
    return jsonify(result="Error", error="Product is deleted")


def success():
    return jsonify(result="Success")

def unauthorised():
    return jsonify(result="Error", error="Unauthorised")
