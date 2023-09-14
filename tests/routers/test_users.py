from fastapi.testclient import TestClient

from tests import test_app, db_session


def test_register_user(test_app):
    response = test_app.post("/register", json={"username": "testuser", "email": "testuser@example.com", "password": "password"})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "username": "testuser", "email": "testuser@example.com"}


def test_login_user(test_app):
    response = test_app.post("/login", json={"username": "testuser", "password": "password"})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "username": "testuser", "email": "testuser@example.com"}
