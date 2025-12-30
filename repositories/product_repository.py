from models.product import Product
from sqlalchemy import func

class ProductRepository:

    def find_all(self, db):
        return db.query(Product).all()

    def find_by_id(self, db, product_id):
        return db.query(Product).filter(Product.id == product_id).first()

    def create(self, db, product):
        db.add(product)
        db.commit()
        db.refresh(product)
        return product

    def update(self, db, product):
        db.commit()
        return product

    def delete(self, db, product):
        db.delete(product)
        db.commit()

    # REPORT
    def report_stock(self, db):
        return db.query(
            func.count(Product.id).label("total_product"),
            func.sum(Product.stock).label("total_stock")
        ).first()
