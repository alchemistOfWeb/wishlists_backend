from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies.auth import get_current_user, get_db
from app.models.user import User
from app.models.wishlist import Wishlist
from app.models.wish_item import WishItem
from app.models.tag import Tag
from app.schemas.wish_item import (
    WishItemCreate,
    WishItemUpdate,
    WishItemStatusUpdate,
)
from app.schemas.tag import TagCreate

router = APIRouter(
    prefix="/wishlist",
    tags=["wishlist"],
)


def _get_tags(
    db: Session,
    tags: list[str],
):
    tag_objects = []

    for tag_name in tags:
        tag = db.query(Tag).filter(Tag.name == tag_name).first()

        if not tag:
            tag = Tag(name=tag_name)
            db.add(tag)

        tag_objects.append(tag)

    return tag_objects


@router.post("/tag")
def create_tag(
    data: TagCreate,
    db: Session = Depends(get_db),
):
    tag = Tag(name=data.name)

    db.add(tag)
    db.commit()

    return tag


@router.get("/")
def get_my_wishlists(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    return (
        db.query(Wishlist)
        .filter(Wishlist.owner_id == user.id)
        .all()
    )


@router.post("/")
def create_wishlist(
    title: str,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    wishlist = Wishlist(
        title=title,
        owner_id=user.id,
    )

    db.add(wishlist)
    db.commit()

    return wishlist


@router.delete("/{wishlist_id}")
def delete_wishlist(
    wishlist_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    wishlist = (
        db.query(Wishlist)
        .filter(
            Wishlist.id == wishlist_id,
            Wishlist.owner_id == user.id,
        )
        .first()
    )

    db.delete(wishlist)
    db.commit()


@router.patch("/{wishlist_id}/archive")
def archive_wishlist(
    wishlist_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    wishlist = (
        db.query(Wishlist)
        .filter(
            Wishlist.id == wishlist_id,
            Wishlist.owner_id == user.id,
        )
        .first()
    )

    wishlist.is_public = False

    db.commit()

    return wishlist


@router.post("/{wishlist_id}/item")
def create_wish_item(
    wishlist_id: int,
    data: WishItemCreate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    tags = _get_tags(db, data.tags)

    wish = WishItem(
        title=data.title,
        description=data.description,
        rate=data.rate,
        expiration_date=data.expiration_date,
        wishlist_id=wishlist_id,
        tags=tags,
    )

    db.add(wish)
    db.commit()

    return wish


@router.patch("/item/{item_id}")
def update_wish_item(
    item_id: int,
    data: WishItemUpdate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    wish = db.query(WishItem).filter(WishItem.id == item_id).first()

    if data.title is not None:
        wish.title = data.title

    if data.description is not None:
        wish.description = data.description

    if data.rate is not None:
        wish.rate = data.rate

    if data.expiration_date is not None:
        wish.expiration_date = data.expiration_date

    if data.tags is not None:
        wish.tags = _get_tags(db, data.tags)

    db.commit()

    return wish


@router.delete("/item/{item_id}")
def delete_wish_item(
    item_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    wish = db.query(WishItem).filter(WishItem.id == item_id).first()

    db.delete(wish)
    db.commit()


@router.get("/{wishlist_id}/items")
def get_wishlist_items(
    wishlist_id: int,
    db: Session = Depends(get_db),
):
    items = (
        db.query(WishItem)
        .filter(
            WishItem.wishlist_id == wishlist_id,
            WishItem.is_deleted == False,
        )
        .all()
    )

    result = []

    for item in items:
        result.append(
            {
                "id": item.id,
                "title": item.title,
                "description": item.description,
                "rate": item.rate,
                "expiration_date": item.expiration_date,
                "is_reserved": item.is_reserved,
                "is_gifted": item.is_gifted,
                "is_delivering": item.is_delivering,
                "is_archieved": item.is_archieved,
                "tags": [tag.name for tag in item.tags],
            }
        )

    return result


@router.post("/item/{item_id}/reserve")
def reserve_item(
    item_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    wish = db.query(WishItem).filter(WishItem.id == item_id).first()

    wish.is_reserved = True
    wish.reserved_by_user_id = user.id

    db.commit()

    return wish


@router.patch("/item/{item_id}/gifted")
def set_gifted(
    item_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    wish = db.query(WishItem).filter(WishItem.id == item_id).first()

    wish.is_gifted = True

    db.commit()

    return wish


@router.patch("/item/{item_id}/is_archieved")
def set_archived(
    item_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    item = db.query(WishItem).filter(WishItem.id == item_id).first()

    item.is_archieved = True

    db.commit()

    return item


@router.patch("/item/{item_id}/is_delivering")
def set_delivering(
    item_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    item = db.query(WishItem).filter(WishItem.id == item_id).first()

    item.is_delivering = True

    db.commit()

    return item


@router.patch("/item/{item_id}/is_gifted")
def set_gifted(
    item_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    item = db.query(WishItem).filter(WishItem.id == item_id).first()

    item.is_gifted = True

    db.commit()

    return item

# @router.patch("/item/{item_id}/status")
# def update_status(
#     item_id: int,
#     data: WishItemStatusUpdate,
#     db: Session = Depends(get_db),
#     user: User = Depends(get_current_user),
# ):
#     wish = db.query(WishItem).filter(WishItem.id == item_id).first()

#     if data.is_gifted is not None:
#         wish.is_gifted = data.is_gifted

#     if data.is_delivering is not None:
#         wish.is_delivering = data.is_delivering

#     if data.is_archieved is not None:
#         wish.is_archieved = data.is_archieved

#     if data.is_deleted is not None:
#         wish.is_deleted = data.is_deleted

#     db.commit()

#     return wish


@router.get("/friend/{user_id}")
def get_friend_wishlist(
    user_id: int,
    db: Session = Depends(get_db),
):
    return (
        db.query(Wishlist)
        .filter(
            Wishlist.owner_id == user_id,
            Wishlist.is_public == True,
        )
        .all()
    )

@router.get("/tags")
def get_tags(
    db: Session = Depends(get_db),
):
    return db.query(Tag).all()
