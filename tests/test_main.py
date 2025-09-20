from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_todo():
    response = client.post("/todos/", json={"title": "Test todo", "description": "Check pytest"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test todo"
    assert "id" in data

def test_read_todos():
    response = client.get("/todos/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
