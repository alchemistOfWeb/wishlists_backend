from sqlalchemy import Column, Integer, String, Date, Boolean

from app.db.base import Base


class GlobalEvent(Base):
    __tablename__ = "global_events"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    is_recurring = Column(Boolean, default=True)
    notify_days_before = Column(Integer, default=7)
