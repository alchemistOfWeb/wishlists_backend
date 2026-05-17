from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base


class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String(512), nullable=True)
    date = Column(Date, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"))
    is_recurring = Column(Boolean, default=True)  
    notify_days_before = Column(Integer, default=7)
    owner = relationship("User")
