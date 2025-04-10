from typing import Annotated
from fastapi import APIRouter, Body, HTTPException, Path
from app.deps import SessionLocal
from app.schemas.genre import GenreCreate
from app.models import Genre
from sqlmodel import select


router = APIRouter(
    prefix="/genres",
    tags=["genres"],
)


# TODO: separate into operations
@router.post("/", status_code=201)
async def create_genre(
    genre_data: Annotated[GenreCreate, Body(title="Genre Data")], db: SessionLocal
) -> Genre:
    genre = Genre(name=genre_data.name)
    db.add(genre)
    db.commit()
    db.refresh(genre)
    return genre


@router.get("/{genre_id}", status_code=200)
async def retrieve_genre(
    genre_id: Annotated[int, Path(title="Genre ID")], db: SessionLocal
) -> Genre:
    genre = db.get(Genre, genre_id)
    if genre is None:
        raise HTTPException(status_code=404, detail="Genre not found")
    return genre


@router.delete("/{genre_id}", status_code=204)
async def delete_genre(
    genre_id: Annotated[int, Path(title="Genre ID")], db: SessionLocal
) -> None:
    genre = db.get(Genre, genre_id)
    if genre is None:
        raise HTTPException(status_code=404, detail="Genre not found")
    db.delete(genre)
    db.commit()
    return None


@router.get("/", status_code=200)
async def list_genre(db: SessionLocal) -> list[Genre]:
    genres = db.exec(select(Genre)).all()
    return genres
