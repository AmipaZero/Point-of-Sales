from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from database.db import Base
from datetime import datetime

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)

    name = Column(String(100), nullable=False)
    price = Column(Numeric(12, 2), nullable=False)
    stock = Column(Integer, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)

    category = relationship("Category")
