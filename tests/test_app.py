import pytest

from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_home_page(client):

    response = client.get("/")

    assert response.status_code == 200


def test_health_page(client):

    response = client.get("/health")

    assert response.status_code == 200
    assert b"Application is healthy" in response.data


def test_add_employee_page(client):

    response = client.get("/add")

    assert response.status_code == 200