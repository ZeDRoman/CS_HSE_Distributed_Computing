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