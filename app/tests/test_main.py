from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_create_meme():
    response = client.post("/memes/", json={"title": "Test Meme", "url": "http://example.com/meme.jpg"})
    assert response.status_code == 200
    assert response.json()["title"] == "Test Meme"
