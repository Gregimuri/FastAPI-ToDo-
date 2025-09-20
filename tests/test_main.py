from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_todo():
    response = client.post("/todos/", json={"title": "Test", "description": "Check", "completed": False})
    assert response.status_code == 200
    assert response.json()["title"] == "Test"

def test_read_todos():
    response = client.get("/todos/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
