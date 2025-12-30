from flask import request
from flask_jwt_extended import get_jwt_identity
from database.db import get_db
from services.auth_service import AuthService
from helpers.response import success, bad_request
from middlewares.jwt_middleware import jwt_required_db


def login():
    db = get_db()
    data = request.json

    token = AuthService().login(db, data["username"], data["password"])
    if not token:
        return bad_request("Invalid credentials")

    return success({
        "token": token
    })


@jwt_required_db
def logout():
    db = get_db()
    user_id = int(get_jwt_identity())

    AuthService().logout(db, user_id)
    return success()
