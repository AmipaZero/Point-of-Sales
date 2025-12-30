from sqlalchemy import Column, Integer, String, DateTime
from database.db import Base
from datetime import datetime

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)
