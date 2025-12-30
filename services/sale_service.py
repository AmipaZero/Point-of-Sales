from sqlalchemy.orm import Session
from models.sale import Sale
from models.sale_detail import SaleDetail
from repositories.sale_repository import SaleRepository
from repositories.product_repository import ProductRepository


class SaleService:

    def get_all(self, db: Session):
        return SaleRepository().find_all(db)

    def get_by_id(self, db: Session, sale_id: int):
        return SaleRepository().find_by_id(db, sale_id)

    def create(self, db: Session, user_id: int, data: dict):
        details_data = data.get("details", [])
        total_price = 0

        sale = Sale(
            user_id=user_id,
            payment_method=data["payment_method"],
            total_price=0
        )

        for item in details_data:
            product = ProductRepository().find_by_id(db, item["product_id"])
            if not product or product.stock < item["qty"]:
                raise ValueError("Invalid product or stock")

            subtotal = product.price * item["qty"]
            total_price += subtotal

            product.stock -= item["qty"]

            detail = SaleDetail(
                product_id=product.id,
                qty=item["qty"],
                price=product.price,
                subtotal=subtotal
            )
            sale.details.append(detail)

        sale.total_price = total_price
        return SaleRepository().save(db, sale)

    def update(self, db: Session, sale_id: int, data: dict):
        sale = SaleRepository().find_by_id(db, sale_id)
        if not sale:
            return None

        sale.payment_method = data.get("payment_method", sale.payment_method)
        db.commit()
        return sale

    def delete(self, db: Session, sale_id: int):
        sale = SaleRepository().find_by_id(db, sale_id)
        if not sale:
            return False

        SaleRepository().delete(db, sale)
        return True

    def report(self, db: Session):
        return SaleRepository().report(db)
