from datetime import date

from fastapi import APIRouter, Depends, Query
from sqlalchemy import case
from sqlalchemy.orm import Session

from app.dependencies.auth import get_db, get_current_user
from app.models.event import Event
from app.models.global_event import GlobalEvent
from app.models.user import User
from app.schemas.event import EventCreate, EventUpdate
from app.services.events import get_upcoming_events as _get_upcoming_events


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
        description=data.description,
        date=data.date,
        is_recurring=data.is_recurring,
        notify_days_before=data.notify_days_before,
        owner_id=user.id,
    )

    db.add(event)
    db.commit()
    db.refresh(event)
    return event


@router.get("/")
def get_my_events(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
    page: int = Query(1, ge=1),
    per_page: int = Query(20, ge=1, le=100),
):
    offset = (page - 1) * per_page
    today = date.today()
    user_events = (
        db.query(Event)
        .filter(Event.owner_id == user.id)
        .order_by(
            case((Event.date < today, 1), else_=0),
            Event.date.asc(),
        )
        .offset(offset)
        .limit(per_page)
        .all()
    )
    return user_events


@router.get("/all")
def get_all_events(
    page: int = Query(1, ge=1),
    per_page: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    offset = (page - 1) * per_page
    user_events = (
        db.query(Event)
        .filter(Event.owner_id == user.id)
        .order_by(Event.date.asc())
        .offset(offset)
        .limit(per_page)
        .all()
    )

    global_events = db.query(GlobalEvent).all()

    return {
        "user_events": user_events,
        "global_events": global_events,
    }

@router.get("/upcoming")
def get_upcoming_events(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    return _get_upcoming_events(db, user)


@router.get("/upcoming/count")
def get_upcoming_events_count(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    events = _get_upcoming_events(db, user)

    return {
        "count": len(events),
    }

# in future it must work only for admins
@router.post("/global")
def create_global_event(
    data: EventCreate,
    db: Session = Depends(get_db),
):
    event = GlobalEvent(
        title=data.title,
        date=data.date,
        is_recurring=data.is_recurring,
        notify_days_before=data.notify_days_before,
    )

    db.add(event)
    db.commit()

    return event


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

    if data.description is not None:
        event.description = data.description

    if data.date is not None:
        event.date = data.date

    if data.is_recurring is not None:
        event.is_recurring = data.is_recurring

    if data.notify_days_before is not None:
        event.notify_days_before = data.notify_days_before


    db.commit()
    db.refresh(event)
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
