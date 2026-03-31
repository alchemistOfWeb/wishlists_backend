from sqlalchemy.orm import Session

from app.models.wish import Wish
from app.models.tag import Tag
from app.models.user import User


def create_wish(
    db: Session,
    user: User,
    data,
):
    tags = []

    for tag_name in data.tags:
        tag = db.query(Tag).filter(Tag.name == tag_name).first()

        if not tag:
            tag = Tag(name=tag_name)
            db.add(tag)

        tags.append(tag)

    wish = Wish(
        product_name=data.product_name,
        description=data.description,
        rate=data.rate,
        expiration_date=data.expiration_date,
        owner_id=user.id,
        tags=tags,
    )

    db.add(wish)
    db.commit()
    db.refresh(wish)

    return wish


def delete_wish(
    db: Session,
    wish: Wish,
):
    db.delete(wish)
    db.commit()
