import requests


class BookerClient:
    """Тонкий клиент для restful-booker: эндпоинты собраны в одном месте,
    тесты дёргают методы, а не URL напрямую (тот же смысл, что Page Object для UI)."""

    def __init__(self, base_url, session=None):
        self.base_url = base_url
        self.session = session or requests.Session()

    def ping(self):
        return self.session.get(f"{self.base_url}/ping")

    def create_booking(self, payload):
        return self.session.post(f"{self.base_url}/booking", json=payload)

    def get_booking(self, booking_id):
        # restful-booker по умолчанию отдаёт XML — просим JSON явно
        return self.session.get(
            f"{self.base_url}/booking/{booking_id}",
            headers={"Accept": "application/json"},
        )

    def auth(self, username, password):
        return self.session.post(
            f"{self.base_url}/auth",
            json={"username": username, "password": password},
        )
