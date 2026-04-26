from fastapi.testclient import TestClient
from api.main import app
import uuid

client = TestClient(app)


def criar_usuario_e_token(email=None):
    email = email or f"teste_{uuid.uuid4()}@test.com"
    client.post("/auth/register", json={"email": email, "senha": "123456"})
    response = client.post("/auth/login", json={"email": email, "senha": "123456"})
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


def test_criar_livro():
    headers = criar_usuario_e_token()
    response = client.post("/livros/", json={
        "titulo": "Clean Code",
        "autor": "Robert Martin",
        "editora": "Prentice Hall",
        "ano": 2008
    }, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["titulo"] == "Clean Code"
    assert "uuid" in data


def test_listar_livros():
    headers = criar_usuario_e_token()
    client.post("/livros/", json={
        "titulo": "The Pragmatic Programmer",
        "autor": "David Thomas",
        "editora": "Addison-Wesley",
        "ano": 1999
    }, headers=headers)
    response = client.get("/livros/", headers=headers)
    assert response.status_code == 200
    assert len(response.json()) >= 1


def test_isolamento_entre_usuarios():
    headers_a = criar_usuario_e_token()
    headers_b = criar_usuario_e_token()

    # usuário A cria um livro
    client.post("/livros/", json={
        "titulo": "Livro do Usuario A",
        "autor": "Autor A",
        "editora": "Editora A",
        "ano": 2020
    }, headers=headers_a)

    # usuário B lista — não deve ver livro do A
    response = client.get("/livros/", headers=headers_b)
    assert response.status_code == 200
    titulos = [l["titulo"] for l in response.json()]
    assert "Livro do Usuario A" not in titulos