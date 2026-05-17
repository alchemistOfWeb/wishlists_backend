from sqlalchemy.orm import Session

from .global_events import seed_global_events


def run_seeds(db: Session):
    seed_global_events(db)
