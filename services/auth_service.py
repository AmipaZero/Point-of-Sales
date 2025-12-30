from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token
from datetime import datetime, timedelta
from repositories.user_repository import UserRepository
from repositories.auth_repository import AuthRepository

class AuthService:

    def login(self, db, username, password):
        user = UserRepository().find_by_username(db, username)

        if not user or not check_password_hash(user.password, password):
            return None

        token = create_access_token(identity=str(user.id))

        expired_at = datetime.utcnow() + timedelta(hours=1)

        AuthRepository().save_token(db, user.id, token, expired_at)
        return token

    def logout(self, db, user_id):
        AuthRepository().delete_token(db, user_id)
