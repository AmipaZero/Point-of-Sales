from models.category import Category
from repositories.category_repository import CategoryRepository

class CategoryService:

    def get_all(self, db):
        return CategoryRepository().find_all(db)

    def create(self, db, data):
        category = Category(name=data["name"])
        return CategoryRepository().create(db, category)

    def delete(self, db, category_id):
        repo = CategoryRepository()
        category = repo.find_by_id(db, category_id)

        if not category:
            return False

        repo.delete(db, category)
        return True
