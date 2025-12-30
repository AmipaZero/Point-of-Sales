from models.user import User

class UserRepository:

    def find_by_id(self, db, user_id: int):
        return db.query(User).filter(User.id == user_id).first()

    def find_by_username(self, db, username: str):
        return db.query(User).filter(User.username == username).first()

    def create(self, db, user: User):
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
