import pytest
from api.booker_client import BookerClient


@pytest.fixture
def client(base_url, api_session):
    return BookerClient(base_url, api_session)


@pytest.fixture
def booking_payload():
    return {
        "firstname": "Daria",
        "lastname": "Larina",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {"checkin": "2026-07-01", "checkout": "2026-07-10"},
        "additionalneeds": "Breakfast",
    }


def test_ping_healthcheck(client):
    """Сервис жив: GET /ping → 201 Created."""
    resp = client.ping()
    assert resp.status_code == 201


def test_create_booking(client, booking_payload):
    """Позитивный: создание брони → 200 и тело содержит наши данные."""
    resp = client.create_booking(booking_payload)
    assert resp.status_code == 200

    body = resp.json()
    assert "bookingid" in body
    assert body["booking"]["firstname"] == booking_payload["firstname"]
    assert body["booking"]["totalprice"] == booking_payload["totalprice"]


def test_get_created_booking(client, booking_payload):
    """Сценарий: создаём бронь → читаем её по id → данные совпадают."""
    booking_id = client.create_booking(booking_payload).json()["bookingid"]

    resp = client.get_booking(booking_id)
    assert resp.status_code == 200

    body = resp.json()
    assert body["firstname"] == booking_payload["firstname"]
    assert body["lastname"] == booking_payload["lastname"]


def test_get_nonexistent_booking_returns_404(client):
    """Негативный: запрос несуществующей брони → 404 Not Found."""
    resp = client.get_booking(999999999)
    assert resp.status_code == 404


def test_auth_returns_token(client):
    """Авторизация валидными данными → 200 и токен в ответе."""
    resp = client.auth("admin", "password123")
    assert resp.status_code == 200
    assert "token" in resp.json()
