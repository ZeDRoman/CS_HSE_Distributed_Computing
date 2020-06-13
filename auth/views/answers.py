from flask import jsonify


def success():
    return jsonify(result="Success")


def invalidLogining():
    return jsonify(result="error", error="Invalid username or password")


def tokenIsRotten():
    return jsonify(result="error", error="You'r refresh token is rotten")


def emailTaken():
    return jsonify(result="error", error="Email is already taken")


def refreshTokenNotProvided():
    return jsonify(result="error", error="Refresh token not provided")


def userEmailIsNotConfirmed():
    return jsonify(result="error", error="Email is not comfired")


def invalidConfirmToken():
    return jsonify(result="error", error="Invalid confirmation url")


def noSuchUser():
    return jsonify(result="Error", error="Email doesn't exists")


def accesEmailNotProvided():
    return jsonify(result="Error", error="Access token or Email not provided")


def notAdmin():
    return jsonify(result="Error", error="Need admin privileges")