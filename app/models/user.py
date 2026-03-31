from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.db.base import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    username = Column(String, unique=True, nullable=False)
    is_active = Column(Boolean, default=True)
    telegram_id = Column(String, nullable=True, unique=True)
    telegram_username = Column(String, nullable=True)
    wishlists = relationship("Wishlist", back_populates="owner")
