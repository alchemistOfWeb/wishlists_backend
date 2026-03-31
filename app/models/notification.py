from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
from app.db.base import Base


class Notification(Base):
    __tablename__ = "notifications"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    type = Column(String)  # telegram / email
    message = Column(String)
    is_sent = Column(Boolean, default=False)
    scheduled_at = Column(DateTime)
    