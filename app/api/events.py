from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies.auth import get_db, get_current_user
from app.models.event import Event
from app.models.user import User
from app.schemas.event import EventCreate, EventUpdate

router = APIRouter(
    prefix="/events",
    tags=["events"],
)


@router.post("/")
def create_event(
    data: EventCreate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    event = Event(
        title=data.title,
        date=data.date,
        is_recurring=data.is_recurring,
        owner_id=user.id,
    )

    db.add(event)
    db.commit()

    return event


@router.get("/")
def get_my_events(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    return (
        db.query(Event)
        .filter(Event.owner_id == user.id)
        .all()
    )


@router.patch("/{event_id}")
def update_event(
    event_id: int,
    data: EventUpdate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    event = (
        db.query(Event)
        .filter(
            Event.id == event_id,
            Event.owner_id == user.id,
        )
        .first()
    )

    if data.title is not None:
        event.title = data.title

    if data.date is not None:
        event.date = data.date

    if data.is_recurring is not None:
        event.is_recurring = data.is_recurring

    db.commit()

    return event


@router.delete("/{event_id}")
def delete_event(
    event_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    event = (
        db.query(Event)
        .filter(
            Event.id == event_id,
            Event.owner_id == user.id,
        )
        .first()
    )

    db.delete(event)
    db.commit()

    return {"status": "ok"}
