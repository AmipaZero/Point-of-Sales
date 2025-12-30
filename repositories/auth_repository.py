from models.user import User

class AuthRepository:

    def save_token(self, db, user_id, token, expired_at):
        user = db.query(User).filter(User.id == user_id).first()
        user.token = token
        user.token_expired_at = expired_at
        db.commit()

    def delete_token(self, db, user_id):
        user = db.query(User).filter(User.id == user_id).first()
        user.token = None
        user.token_expired_at = None
        db.commit()
