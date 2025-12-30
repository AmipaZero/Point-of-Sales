from flask import request
from database.db import get_db
from services.category_service import CategoryService
from helpers.response import success, bad_request
from middlewares.jwt_middleware import jwt_required_db


@jwt_required_db
def get_categories():
    db = get_db()
    categories = CategoryService().get_all(db)

    return success([
        {
            "id": c.id,
            "name": c.name,
            "created_at": c.created_at
        } for c in categories
    ])


@jwt_required_db
def create_category():
    db = get_db()
    data = request.json

    if "name" not in data:
        return bad_request("Category name is required")

    CategoryService().create(db, data)
    return success(code=201)


@jwt_required_db
def delete_category(category_id):
    db = get_db()
    success_delete = CategoryService().delete(db, category_id)

    if not success_delete:
        return bad_request("Category not found")

    return success()
