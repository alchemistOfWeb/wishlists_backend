from sqlalchemy.orm import Session

from app.models.user import User
from app.core.security import hash_password, verify_password, create_access_token


def sign_up(db: Session, email: str, username: str, password: str) -> User:
    user = User(
        email=email,
        username=username,
        password_hash=hash_password(password),
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def sign_in(db: Session, login: str, password: str):
    user = (
        db.query(User)
        .filter(
            (User.email == login) |
            (User.username == login)
        )
        .first()
    )

    if not user:
        return None

    if not verify_password(password, user.password_hash):
        return None

    return create_access_token({"user_id": user.id})
