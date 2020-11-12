from flask import jsonify


def success():
    return jsonify(error="Success")


def invalidLogining():
    return jsonify(error="Invalid username or password")


def tokenIsRotten():
    return jsonify(error="You'r refresh token is rotten")


def emailTaken():
    return jsonify(error="Email is already taken")

def refreshTokenNotProvided():
    return jsonify(error="Refresh token not provided")