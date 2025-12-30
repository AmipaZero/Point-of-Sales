from flask import Blueprint
from controllers.sale_controller import (
    get_sales,
    get_sale,
    create_sale,
    update_sale,
    delete_sale,
    sale_report
)

sale_bp = Blueprint("sale", __name__)

sale_bp.get("/")(get_sales)
sale_bp.get("/<int:sale_id>")(get_sale)
sale_bp.post("/")(create_sale)
sale_bp.put("/<int:sale_id>")(update_sale)
sale_bp.delete("/<int:sale_id>")(delete_sale)
sale_bp.get("/report")(sale_report)
