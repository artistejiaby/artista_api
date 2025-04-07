from pydantic import BaseModel, EmailStr, FilePath
from datetime import datetime
from typing import Optional


class UserBase(BaseModel):
    email: EmailStr
    password: str


class UserCreate(UserBase):
    hashed_password: str


class User(UserBase):
    id: int
    name: str
    email: EmailStr
    is_active: bool
    last_login: datetime
    photo: Optional[FilePath]
