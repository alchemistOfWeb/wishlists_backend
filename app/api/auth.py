from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.schemas.auth import SignUpSchema, TokenSchema
from app.services.auth import sign_up, sign_in
from app.dependencies.auth import get_db
from app.constants.auth import TOKEN_TYPE

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/sign-up", response_model=TokenSchema)
def sign_up_route(
    data: SignUpSchema,
    db: Session = Depends(get_db),
):
    user = sign_up(
        db,
        data.email,
        data.username,
        data.password,
    )

    token = sign_in(
        db,
        data.email,
        data.password,
    )

    return {
        "access_token": token,
        "token_type": TOKEN_TYPE,
    }


@router.post("/sign-in", response_model=TokenSchema)
def sign_in_route(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    token = sign_in(
        db,
        form_data.username,
        form_data.password,
    )

    if not token:
        raise HTTPException(status_code=401)

    return {
        "access_token": token,
        "token_type": TOKEN_TYPE,
    }


@router.post("/sign-out")
def sign_out():
    return {"message": "ok"}
