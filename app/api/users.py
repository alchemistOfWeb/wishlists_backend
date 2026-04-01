from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.dependencies.auth import get_db, get_current_user
from app.models.user import User

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/search")
def search_users(
    username: str = Query(..., min_length=1),
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    users = (
        db.query(User)
        .filter(
            User.username.ilike(f"%{username}%"),
            User.id != user.id,
        )
        .limit(20)
        .all()
    )

    return [
        {
            "id": u.id,
            "username": u.username,
        }
        for u in users
    ]


@router.get("/me")
def get_me(current_user: User = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "email": current_user.email,
        "username": current_user.username,
    }

@router.get("/{id}")
def get_user(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        return {"error": "User not found"}
    return {
        "id": user.id,
        "email": user.email,
        "username": user.username,
    }
