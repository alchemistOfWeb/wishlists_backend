from datetime import date
from sqlalchemy.orm import Session
from app.models.global_event import GlobalEvent


DEFAULT_NOTIFY_DAYS = 7

NEW_YEAR_MONTH = 1
NEW_YEAR_DAY = 1

MARCH_8_MONTH = 3
MARCH_8_DAY = 8

FEBRUARY_23_MONTH = 2
FEBRUARY_23_DAY = 23


def seed_global_events(db: Session):
    year = date.today().year

    events = [
        {
            "title": "New Year",
            "date": date(year, NEW_YEAR_MONTH, NEW_YEAR_DAY),
        },
        {
            "title": "International Women's Day",
            "date": date(year, MARCH_8_MONTH, MARCH_8_DAY),
        },
        {
            "title": "Defender of the Fatherland Day",
            "date": date(year, FEBRUARY_23_MONTH, FEBRUARY_23_DAY),
        },
    ]

    for event in events:
        exists = (
            db.query(GlobalEvent)
            .filter(GlobalEvent.title == event["title"])
            .first()
        )

        if exists:
            continue

        db.add(
            GlobalEvent(
                title=event["title"],
                date=event["date"],
                notify_days_before=DEFAULT_NOTIFY_DAYS,
                is_recurring=True,
            )
        )

    db.commit()