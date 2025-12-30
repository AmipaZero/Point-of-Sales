from flask import Blueprint
from controllers.product_controller import (
    get_products,
    get_product,
    create_product,
    update_product,
    delete_product,
    product_report
)

product_bp = Blueprint("product", __name__)

product_bp.get("/")(get_products)
product_bp.get("/<int:product_id>")(get_product)
product_bp.post("/")(create_product)
product_bp.put("/<int:product_id>")(update_product)
product_bp.delete("/<int:product_id>")(delete_product)

product_bp.get("/report")(product_report)
