from datetime import datetime, UTC

from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Boolean,
    DateTime,
)
from sqlalchemy.orm import relationship

from app.db.base import Base


class WishItem(Base):
    __tablename__ = "wish_items"

    id = Column(Integer, primary_key=True)

    title = Column(String, nullable=False)
    description = Column(String)
    link = Column(String)
    price = Column(Integer)

    rate = Column(Integer)

    expiration_date = Column(DateTime(timezone=True), nullable=True)

    wishlist_id = Column(
        Integer,
        ForeignKey("wishlists.id"),
    )

    reserved_by_user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=True,
    )

    is_reserved = Column(Boolean, default=False)

    is_gifted = Column(Boolean, default=False)
    is_delivering = Column(Boolean, default=False)
    is_archieved = Column(Boolean, default=False)
    is_deleted = Column(Boolean, default=False)

    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
    )

    wishlist = relationship(
        "Wishlist",
        back_populates="items",
    )

    tags = relationship(
        "Tag",
        secondary="wish_item_tags",
        back_populates="items",
    )