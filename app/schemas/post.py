from pydantic import BaseModel, FilePath
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .artist import Artist


class PostBase(BaseModel):
    title: str
    description: str
    file: Optional[FilePath]
    artist: "Artist"


class PostCreate(PostBase):
    pass
