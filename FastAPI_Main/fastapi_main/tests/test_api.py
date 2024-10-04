
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_product():
    """Test creating a new product."""
    response = client.post("/api/products/", json={"name": "Product1", "description": "A sample product", "price": 10.99})
    assert response.status_code == 200
    assert response.json()["name"] == "Product1"

def test_get_product():
    """Test retrieving a product by ID."""
    response = client.get("/api/products/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Product1"

def test_update_product():
    """Test updating an existing product."""
    response = client.put("/api/products/1", json={"name": "Updated Product", "description": "Updated description", "price": 12.99})
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Product"

def test_delete_product():
    """Test deleting a product by ID."""
    response = client.delete("/api/products/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Product"
