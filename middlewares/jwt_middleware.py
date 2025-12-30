from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from functools import wraps
from flask import g
from database.db import get_db
from repositories.user_repository import UserRepository

def jwt_required_db(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()

        user_id = int(get_jwt_identity())
        db = get_db()

        user = UserRepository().find_by_id(db, user_id)

        if not user or not user.token:
            return {"message": "Unauthorized"}, 401

        g.current_user = user   
        g.db = db               

        return fn(*args, **kwargs)
    return wrapper
