from werkzeug.security import generate_password_hash
from repositories.user_repository import UserRepository
from models.user import User

class UserService:

    def __init__(self):
        self.repo = UserRepository()

    def register(self, db, data: dict) -> User:
        user = User(
            name=data["name"],
            username=data["username"],
            password=generate_password_hash(data["password"]),
            role=data.get("role", "CASHIER")
        )
        return self.repo.create(db, user)

    def get_by_id(self, db, user_id: int) -> User | None:
        return self.repo.find_by_id(db, user_id)
