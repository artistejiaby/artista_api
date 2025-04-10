from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import genres
from contextlib import asynccontextmanager
from .db import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting Database")
    init_db()
    yield


app = FastAPI(lifespan=lifespan, title="Artista API", description="API for artistas")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(genres.router)
