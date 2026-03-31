from pydantic import BaseModel


class SignUpSchema(BaseModel):
    email: str
    username: str
    password: str


class SignInSchema(BaseModel):
    email: str
    password: str


class TokenSchema(BaseModel):
    access_token: str
    token_type: str = "bearer"
