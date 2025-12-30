from flask import jsonify


def success(data=None, message="OK", code=200):
    return jsonify({
        "code": code,
        "status": "OK",
        "message": message,
        "data": data or {}
    }), code


def bad_request(message="Bad Request"):
    return jsonify({
        "code": 400,
        "status": "BAD_REQUEST",
        "message": message
    }), 400


def unauthorized(message="Unauthorized"):
    return jsonify({
        "code": 401,
        "status": "UNAUTHORIZED",
        "message": message
    }), 401


def internal_error(message="Internal Server Error"):
    return jsonify({
        "code": 500,
        "status": "ERROR",
        "message": message
    }), 500
