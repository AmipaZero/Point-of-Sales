from flask import Blueprint
from controllers.auth_controller import login, logout

auth_bp = Blueprint("auth", __name__)
auth_bp.post("/login")(login)
auth_bp.delete("/logout")(logout)
