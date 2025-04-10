from .db import engine
from sqlmodel import Session
from typing import Annotated
from fastapi import Depends


def get_session():
    with Session(engine) as session:
        yield session


SessionLocal = Annotated[Session, Depends(get_session)]
