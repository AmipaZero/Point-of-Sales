from sqlalchemy import Column, Integer, DateTime, ForeignKey, Numeric, String
from sqlalchemy.orm import relationship
from datetime import datetime
from database.db import Base

class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    total_price = Column(Numeric(12, 2), nullable=False)
    payment_method = Column(String(20), nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User")
    details = relationship(
        "SaleDetail",
        back_populates="sale",
        cascade="all, delete"
    )
