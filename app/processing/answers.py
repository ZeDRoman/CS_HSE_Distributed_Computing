from flask import jsonify


def idDoesntExists(product_id):
    return jsonify(error=F"Object with id = {product_id} doesnt exist")


def idNotNumber():
    return jsonify(error="Id must be number")


def pageNotNumber():
    return jsonify(error="Page must be number")


def pageCountNotNumber():
    return jsonify(error="Page count must be number")


def idExists():
    return jsonify(error="Product with that id already exists")


def productCreated():
    return jsonify(error="Product is created")


def productEdited():
    return jsonify(error="Product is edited")


def productDeleted():
    return jsonify(error="Product is deleted")


def success():
    return jsonify(error="Success")


def loggedIn():
    return jsonify(error="You are already logged in")


def invalidLoging():
    return jsonify(error="Invalid username or password")


def tokenIsRotten():
    return jsonify(error="You'r refresh token is rotten")

def emailTaken():
    return jsonify(error="Email is already taken")
