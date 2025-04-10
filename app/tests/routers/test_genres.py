def test_create_genre(session):
    response = session.post("/genres/", json={"name": "Pop"})
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Pop"


def test_retrieve_genre(session, fake_genre):
    response = session.get(f"/genres/{fake_genre.id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == fake_genre.name


def test_list_genre(session, fake_genre):
    response = session.get("/genres/")
    assert response.status_code == 200
    data = response.json()
    assert data[0]["name"] == fake_genre.name
