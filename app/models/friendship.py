from sqlalchemy import Column, Integer, ForeignKey,Boolean, UniqueConstraint
from app.db.base import Base


# class Friendship(Base):
#     __tablename__ = "friendships"
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey("users.id"))
#     friend_id = Column(Integer, ForeignKey("users.id"))
#     __table_args__ = (
#         UniqueConstraint("user_id", "friend_id"),
#     )


class Friendship(Base):
    __tablename__ = "friendships"

    id = Column(Integer, primary_key=True)

    follower_id = Column(
        Integer,
        ForeignKey("users.id"),
    )

    following_id = Column(
        Integer,
        ForeignKey("users.id"),
    )

    is_mutual = Column(Boolean, default=False)

