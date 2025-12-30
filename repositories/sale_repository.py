from sqlalchemy.orm import Session
from sqlalchemy import func
from models.sale import Sale
from models.sale_detail import SaleDetail


class SaleRepository:

    def find_all(self, db: Session):
        return db.query(Sale).all()

    def find_by_id(self, db: Session, sale_id: int):
        return db.query(Sale).filter(Sale.id == sale_id).first()

    def save(self, db: Session, sale: Sale):
        db.add(sale)
        db.commit()
        db.refresh(sale)
        return sale

    def delete(self, db: Session, sale: Sale):
        db.delete(sale)
        db.commit()

    def report(self, db: Session):
        return db.query(
            func.count(Sale.id).label("total_transaction"),
            func.sum(Sale.total_price).label("total_income")
        ).first()
