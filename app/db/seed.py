from .session import SessionLocal
from .seeds import run_seeds


def seed():
    db = SessionLocal()

    try:
        run_seeds(db)
    finally:
        db.close()

if __name__ == "__main__":
    seed()
