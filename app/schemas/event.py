import datetime

from pydantic import BaseModel


class EventCreate(BaseModel):
    title: str
    date: datetime.date
    is_recurring: bool = True


class EventUpdate(BaseModel):
    title: str | None = None
    date: datetime.date | None = None
    is_recurring: bool | None = None
