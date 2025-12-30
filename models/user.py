from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database.db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    username = Column(String(50), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(String(20), nullable=False)

    token = Column(String, nullable=True)
    token_expired_at = Column(DateTime, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)
