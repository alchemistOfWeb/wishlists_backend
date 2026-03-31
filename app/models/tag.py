from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base import Base


class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True)

    name = Column(String, unique=True, nullable=False)

    items = relationship(
        "WishItem",
        secondary="wish_item_tags",
        back_populates="tags",
    )
