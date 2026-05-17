from datetime import date, timedelta

from sqlalchemy.orm import Session

from app.models.event import Event
from app.models.global_event import GlobalEvent
from app.models.user import User


def get_upcoming_events(
    db: Session,
    user: User,
):
    today = date.today()

    user_events = (
        db.query(Event)
        .filter(Event.owner_id == user.id)
        .all()
    )

    global_events = db.query(GlobalEvent).all()

    result = []

    for event in user_events:
        notify_date = event.date - timedelta(
            days=event.notify_days_before,
        )

        if notify_date <= today <= event.date:
            result.append(event)

    for event in global_events:
        notify_date = event.date - timedelta(
            days=event.notify_days_before,
        )

        if notify_date <= today <= event.date:
            result.append(event)

    return result