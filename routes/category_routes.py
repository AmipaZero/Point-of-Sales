from flask import Blueprint
from controllers.category_controller import (
    get_categories,
    create_category,
    delete_category
)

category_bp = Blueprint("category", __name__)

category_bp.get("/")(get_categories)
category_bp.post("/")(create_category)
category_bp.delete("/<int:category_id>")(delete_category)
