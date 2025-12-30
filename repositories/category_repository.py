from models.category import Category

class CategoryRepository:

    def find_all(self, db):
        return db.query(Category).all()

    def find_by_id(self, db, category_id):
        return db.query(Category).filter(Category.id == category_id).first()

    def find_by_name(self, db, name):
        return db.query(Category).filter(Category.name == name).first()

    def create(self, db, category):
        db.add(category)
        db.commit()
        db.refresh(category)
        return category

    def delete(self, db, category):
        db.delete(category)
        db.commit()
