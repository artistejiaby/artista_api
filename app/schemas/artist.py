from __future__ import annotations
from pydantic import BaseModel
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .genre import Genre
    from .user import User


class ArtistBase(BaseModel):
    genre: "Genre"
    user: "User"


class ArtistCreate(ArtistBase):
    pass


class Artist(ArtistBase):
    id: int
