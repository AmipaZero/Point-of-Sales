from models.product import Product
from repositories.product_repository import ProductRepository

class ProductService:

    def get_all(self, db):
        return ProductRepository().find_all(db)

    def get_by_id(self, db, product_id):
        return ProductRepository().find_by_id(db, product_id)

    def create(self, db, data):
        product = Product(
            category_id=data["category_id"],
            name=data["name"],
            price=data["price"],
            stock=data["stock"]
        )
        return ProductRepository().create(db, product)

    def update(self, db, product_id, data):
        repo = ProductRepository()
        product = repo.find_by_id(db, product_id)

        if not product:
            return None

        product.name = data.get("name", product.name)
        product.price = data.get("price", product.price)
        product.stock = data.get("stock", product.stock)
        product.category_id = data.get("category_id", product.category_id)

        return repo.update(db, product)

    def delete(self, db, product_id):
        repo = ProductRepository()
        product = repo.find_by_id(db, product_id)

        if not product:
            return False

        repo.delete(db, product)
        return True

    def report(self, db):
        return ProductRepository().report_stock(db)
