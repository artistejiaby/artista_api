from datetime import datetime
from sqlmodel import Field, Relationship, SQLModel
from typing import Optional


class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    email: str = Field(default=None, unique=True, index=True)
    password: str = Field(default=None)
    is_active: bool = Field(default=False)
    last_login: datetime = Field(default=None)
    photo: str = Field(default=None)
    artist: Optional["Artist"] = Relationship(
        back_populates="user", sa_relationship_kwargs={"uselist": False}
    )


class Genre(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True, index=True)
    name: str = Field(default=None)
    artists: list["Artist"] = Relationship(back_populates="genre")


class Artist(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True, index=True)
    genre_id: int = Field(default=None, foreign_key="genre.id")
    user_id: int = Field(default=None, foreign_key="user.id")
    genre: Genre = Relationship(back_populates="artists")
    user: User = Relationship(back_populates="artist")
    posts: list["Post"] = Relationship(back_populates="artist")


class Post(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True, index=True)
    title: str = Field(default=None)
    description: str = Field(default=None)
    file: str = Field(default=None)
    artist_id: int = Field(default=None, foreign_key="artist.id")
    artist: Artist = Relationship(back_populates="posts")
