from pydantic import BaseModel
from typing import Union

class BaseUser(BaseModel):
    email: str
    username: str


class UserCreate(BaseUser):
    position: str
    password: str


class User(BaseUser):
    id: int

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    email: str
    password: str


class UserFullInfo(BaseUser):
    id: int
    position: str = None

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str = 'bearer'