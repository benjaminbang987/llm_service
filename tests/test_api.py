import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture
def client():
    return TestClient(app)

def test_predict_endpoint(client):
    response = client.post("/predict", json={"text": "Hello world"})
    assert response.status_code == 200
    assert "probabilities" in response.json()
    assert isinstance(response.json()["probabilities"], list)

def test_predict_empty_text(client):
    response = client.post("/predict", json={"text": ""})
    assert response.status_code == 422  # Manual validation error

def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}