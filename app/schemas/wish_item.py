from datetime import datetime
from typing import List

from pydantic import BaseModel


class WishItemCreate(BaseModel):
    title: str
    description: str | None = None
    rate: int
    tags: List[str] = []
    expiration_date: datetime | None = None


class WishItemUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    rate: int | None = None
    tags: list[str] | None = None
    expiration_date: datetime | None = None


class WishItemStatusUpdate(BaseModel):
    is_gifted: bool | None = None
    is_delivering: bool | None = None
    is_archieved: bool | None = None
    is_deleted: bool | None = None