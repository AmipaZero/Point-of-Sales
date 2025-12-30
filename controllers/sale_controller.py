from flask import request
from flask_jwt_extended import get_jwt_identity
from database.db import get_db
from services.sale_service import SaleService
from helpers.response import success, bad_request
from middlewares.jwt_middleware import jwt_required_db
from middlewares.role_middleware import admin_only


@jwt_required_db
def get_sales():
    db = get_db()
    sales = SaleService().get_all(db)

    return success(data=[
        {
            "id": s.id,
            "user_id": s.user_id,
            "total_price": float(s.total_price),
            "payment_method": s.payment_method,
            "created_at": s.created_at.isoformat()
        } for s in sales
    ])


@jwt_required_db
def get_sale(sale_id):
    db = get_db()
    sale = SaleService().get_by_id(db, sale_id)

    if not sale:
        return bad_request("Sale not found")

    return success(data={
        "id": sale.id,
        "user_id": sale.user_id,
        "total_price": float(sale.total_price),
        "payment_method": sale.payment_method,
        "created_at": sale.created_at.isoformat(),
        "details": [
            {
                "product_id": d.product_id,
                "qty": d.qty,
                "price": float(d.price),
                "subtotal": float(d.subtotal)
            } for d in sale.details
        ]
    })


@jwt_required_db
def create_sale():
    db = get_db()
    user_id = int(get_jwt_identity())

    try:
        sale = SaleService().create(db, user_id, request.json)
        return success(data={"id": sale.id}, message="Sale created", code=201)
    except ValueError as e:
        return bad_request(str(e))


@jwt_required_db
def update_sale(sale_id):
    db = get_db()
    sale = SaleService().update(db, sale_id, request.json)

    if not sale:
        return bad_request("Sale not found")

    return success(message="Sale updated")


@jwt_required_db
def delete_sale(sale_id):
    db = get_db()
    deleted = SaleService().delete(db, sale_id)

    if not deleted:
        return bad_request("Sale not found")

    return success(message="Sale deleted")


@jwt_required_db
@admin_only
def sale_report():
    db = get_db()
    report = SaleService().report(db)

    return success(data={
        "total_transaction": report.total_transaction,
        "total_income": float(report.total_income or 0)
    })
