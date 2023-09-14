from fastapi.testclient import TestClient

from tests import test_app, db_session


def test_get_products(test_app):
    response = test_app.get("/products/")
    assert response.status_code == 200
    assert response.json() == []


def test_create_product(test_app):
    response = test_app.post("/products/", json={"name": "Laptop", "description": "Powerful laptop", "price": 1000, "category_id": 1})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Laptop", "description": "Powerful laptop", "price": 1000, "category": {'id': 1, 'name': 'Electronics'}}
