from flask import request, g
from services.user_service import UserService
from helpers.response import success
from middlewares.jwt_middleware import jwt_required_db
from database.db import get_db


def register():
    db = get_db()
    UserService().register(db, request.json)

    return success(code=201)


@jwt_required_db
def current_user():
    user = g.current_user  

    return success({
        "id": user.id,
        "name": user.name,
        "username": user.username,
        "role": user.role
    })
