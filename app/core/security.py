from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext


from app.constants.auth import (
    ACCESS_TOKEN_EXPIRE_MINUTES,
    ALGORITHM,
    PASSWORD_HASH_SCHEME,
)
from app.core.config import settings

pwd_context = CryptContext(schemes=[PASSWORD_HASH_SCHEME], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def create_access_token(data: dict) -> str:
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    data.update({"exp": expire})
    return jwt.encode(data, settings.SECRET_KEY, algorithm=ALGORITHM)
