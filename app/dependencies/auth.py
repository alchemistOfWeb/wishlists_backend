from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from sqlalchemy.orm import Session

from app.constants.auth import ALGORITHM
from app.core.config import settings
from app.db.session import SessionLocal
from app.models.user import User


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="auth/sign-in"
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
):
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[ALGORITHM],
        )

    except Exception:
        raise HTTPException(status_code=401)

    user_id = payload.get("user_id")

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=401)

    return user