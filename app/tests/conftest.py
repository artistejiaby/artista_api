import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine
from app.deps import get_session
from app.main import app
from app.models import Genre, User, Artist, Post

DATABASE_URL_TEST = "sqlite:///./test.db"

engine_test = create_engine(DATABASE_URL_TEST)


@pytest.fixture
def db():
    SQLModel.metadata.drop_all(engine_test)
    SQLModel.metadata.create_all(engine_test)
    with Session(engine_test) as session:
        yield session


@pytest.fixture
def session(db):
    def override_get_session():
        with Session(engine_test) as session:
            yield session

    app.dependency_overrides[get_session] = override_get_session
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()


@pytest.fixture()
def fake_genre(db):
    genre = Genre(name="Rock")
    db.add(genre)
    db.commit()
    db.refresh(genre)
    return genre


@pytest.fixture()
def fake_user(db):
    user = User(email="test@example.com", password="password")
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@pytest.fixture()
def fake_artist(db, fake_genre, fake_user):
    artist = Artist(genre_id=fake_genre.id, user_id=fake_user.id)
    db.add(artist)
    db.commit()
    db.refresh(artist)
    return artist


@pytest.fixture()
def fake_post(db, fake_artist):
    post = Post(
        title="Test Post",
        description="Test Description",
        file="test.jpg",
        artist_id=fake_artist.id,
    )
    db.add(post)
    db.commit()
    db.refresh(post)
    return post
