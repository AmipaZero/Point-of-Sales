from flask import request
from database.db import get_db
from services.product_service import ProductService
from helpers.response import success, bad_request
from middlewares.jwt_middleware import jwt_required_db
from middlewares.role_middleware import admin_only


@jwt_required_db
def get_products():
    db = get_db()
    products = ProductService().get_all(db)

    return success([
        {
            "id": p.id,
            "category_id": p.category_id,
            "name": p.name,
            "price": float(p.price),
            "stock": p.stock,
            "created_at": p.created_at
        } for p in products
    ])


@jwt_required_db
def get_product(product_id):
    db = get_db()
    product = ProductService().get_by_id(db, product_id)

    if not product:
        return bad_request("Product not found")

    return success({
        "id": product.id,
        "category_id": product.category_id,
        "name": product.name,
        "price": float(product.price),
        "stock": product.stock,
        "created_at": product.created_at
    })


@jwt_required_db
def create_product():
    db = get_db()
    data = request.json

    ProductService().create(db, data)
    return success(code=201)


@jwt_required_db
def update_product(product_id):
    db = get_db()
    product = ProductService().update(db, product_id, request.json)

    if not product:
        return bad_request("Product not found")

    return success()


@jwt_required_db
def delete_product(product_id):
    db = get_db()
    deleted = ProductService().delete(db, product_id)

    if not deleted:
        return bad_request("Product not found")

    return success()


# 🔥 ADMIN ONLY REPORT
@jwt_required_db
@admin_only
def product_report():
    db = get_db()
    report = ProductService().report(db)

    return success({
        "total_product": report.total_product,
        "total_stock": int(report.total_stock or 0)
    })
