from sqlalchemy import Column, Integer, ForeignKey

from app.db.base import Base


class WishItemTag(Base):
    __tablename__ = "wish_item_tags"

    wish_item_id = Column(
        Integer,
        ForeignKey("wish_items.id"),
        primary_key=True,
    )

    tag_id = Column(
        Integer,
        ForeignKey("tags.id"),
        primary_key=True,
    )
