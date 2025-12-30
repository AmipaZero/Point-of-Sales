from flask import Blueprint
from controllers.user_controller import register, current_user

user_bp = Blueprint("user", __name__)
user_bp.post("/register")(register)
user_bp.get("/current")(current_user)
