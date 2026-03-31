from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies.auth import get_db, get_current_user
from app.models.user import User
from app.models.friendship import Friendship

router = APIRouter(
    prefix="/friends",
    tags=["friends"],
)



@router.post("/follow/{user_id}")
def follow_user(
    user_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    friendship = Friendship(
        follower_id=user.id,
        following_id=user_id,
    )

    db.add(friendship)
    db.commit()

    reverse = (
        db.query(Friendship)
        .filter(
            Friendship.follower_id == user_id,
            Friendship.following_id == user.id,
        )
        .first()
    )

    if reverse:
        reverse.is_mutual = True
        friendship.is_mutual = True
        db.commit()

    return {"status": "ok"}