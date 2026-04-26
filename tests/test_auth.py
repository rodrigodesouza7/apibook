from fastapi.testclient import TestClient
from api.main import app
import uuid

client = TestClient(app)


def test_register_and_login():
    email = f"teste_{uuid.uuid4()}@test.com"

    response = client.post("/auth/register", json={
        "email": email,
        "senha": "123456"
    })
    assert response.status_code == 200

    response = client.post("/auth/login", json={
        "email": email,
        "senha": "123456"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()