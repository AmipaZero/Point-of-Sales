from functools import wraps
from flask_jwt_extended import get_jwt_identity
from database.db import get_db
from repositories.user_repository import UserRepository
from helpers.response import unauthorized


def admin_only(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        db = get_db()
        user_id = int(get_jwt_identity())

        user = UserRepository().find_by_id(db, user_id)
        if not user or user.role.lower() != "admin":
            return unauthorized("Admin only")

        return fn(*args, **kwargs)
    return wrapper
