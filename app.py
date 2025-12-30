from flask import Flask
from flask_jwt_extended import JWTManager
from config import Config
from database.db import engine, Base

# routes
from routes.auth_routes import auth_bp
from routes.user_routes import user_bp
from routes.product_routes import product_bp
from routes.category_routes import category_bp
from routes.sale_routes import sale_bp
def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = Config.SECRET_KEY
    app.config["JWT_SECRET_KEY"] = Config.JWT_SECRET_KEY
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = Config.JWT_ACCESS_TOKEN_EXPIRES
    JWTManager(app)
    Base.metadata.create_all(bind=engine)
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(user_bp, url_prefix="/api/users")
    app.register_blueprint(
            category_bp,
            url_prefix="/api/categories"
    )


    app.register_blueprint(
        product_bp,
        url_prefix="/api/products"
    )
   
    app.register_blueprint(
        sale_bp, 
        url_prefix="/api/sales"
    )
    @app.get("/")
    def index():
        return {
            "status": "OK",
            "message": "POS Flask API running"
        }

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
