from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_home():
    response = client.get(
        "/", headers={"content-type": "text/html; charset=utf-8"})
    assert response.status_code == 200
    assert b"Welcome to FastAPI Website Starter Demo" in response.content
    response = client.get("/static/css/style3.css")
    assert response.status_code == 200


def test_page_about():
    response = client.get("/page/about",
                          headers={"content-type": "text/html; charset=utf-8"})
    assert response.status_code == 200
    assert b"About" in response.content


def test_unsplash():
    response = client.get("/unsplash",
                          headers={"content-type": "text/html; charset=utf-8"})
    assert response.status_code == 200
    assert b"Unsplash Finder" in response.content


def test_two_forms():
    response = client.get("/twoforms",
                          headers={"content-type": "text/html; charset=utf-8"})
    assert response.status_code == 200
    assert b"Two Forms" in response.content


def test_accordion():
    response = client.post("/accordion", data={"tag": "flower"}, headers={
                           "Content-Type": "application/x-www-form-urlencoded"})
    assert response.status_code == 200
    assert b"Accordion" in response.content
