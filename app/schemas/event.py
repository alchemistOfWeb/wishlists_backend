import datetime

from pydantic import BaseModel


class EventCreate(BaseModel):
    title: str
    description: str | None = None
    date: datetime.date
    is_recurring: bool = True
    notify_days_before: int | None = None


class EventUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    date: datetime.date | None = None
    is_recurring: bool | None = None
    notify_days_before: int | None = None
