
from tests import test_app, db_session


def test_get_categories(test_app):
    response = test_app.get("/categories/")
    assert response.status_code == 200
    assert response.json() == []


def test_create_category(test_app):
    response = test_app.post("/categories/", json={"name": "Electronics"})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Electronics"}
