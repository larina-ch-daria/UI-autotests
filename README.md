# QA Automation: UI + API

Учебные автотесты: UI на Selenium и API на requests.
**Стек:** Python, Selenium, pytest, requests
**Архитектура:** Page Object Model (UI) + тонкий клиент-обёртка (API)

## UI-тесты — [saucedemo.com](https://www.saucedemo.com/)

| Тест | Тип | Проверка |
|------|-----|----------|
| `test_successful_login` | позитивный | вход с валидными данными → страница товаров |
| `test_login_with_wrong_password` | негативный | неверный пароль → сообщение об ошибке |
| `test_locked_out_user` | негативный | заблокированный пользователь → ошибка блокировки |
| `test_add_item_to_cart` | сценарий | вход → добавление товара → счётчик корзины = 1 |

## API-тесты — [restful-booker](https://restful-booker.herokuapp.com/)

| Тест | Тип | Проверка |
|------|-----|----------|
| `test_ping_healthcheck` | smoke | `GET /ping` → 201 |
| `test_create_booking` | позитивный | `POST /booking` → 200, тело содержит отправленные данные |
| `test_get_created_booking` | сценарий | создать бронь → прочитать по id → данные совпадают |
| `test_get_nonexistent_booking_returns_404` | негативный | запрос несуществующей брони → 404 |
| `test_auth_returns_token` | позитивный | `POST /auth` → 200, токен в ответе |

## Структура

```
.
├── pages/                 # Page Object — классы UI-страниц
│   ├── base_page.py       # базовый класс: общие методы + явные ожидания
│   ├── login_page.py      # страница логина
│   └── inventory_page.py  # страница товаров
├── api/
│   └── booker_client.py   # тонкий клиент API: эндпоинты в одном месте
├── tests/
│   ├── test_login.py        # UI-тесты
│   └── test_booking_api.py  # API-тесты
├── conftest.py            # общие фикстуры: драйвер (UI), base_url и сессия (API)
├── requirements.txt
└── README.md
```

## Запуск

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt

pytest -v                       # все тесты
pytest tests/test_login.py -v        # только UI
pytest tests/test_booking_api.py -v  # только API
```

Selenium 4 сам подтягивает драйвер браузера через Selenium Manager — отдельно ставить chromedriver не нужно.

## Технические решения

- **Page Object Model (UI)** — локаторы и действия хранятся в классах страниц, тесты не обращаются к локаторам напрямую. При изменении вёрстки правка в одном месте.
- **Клиент-обёртка (API)** — эндпоинты собраны в `BookerClient`, тесты дёргают методы, а не URL. Тот же принцип, что POM.
- **Явные ожидания** (`WebDriverWait`) вместо `time.sleep()` — ждём ровно до выполнения условия.
- **Фикстуры в `conftest.py`** через `yield`: setup до, teardown после (закрытие браузера/сессии срабатывает даже при падении теста).
- **Изоляция тестов** — каждый тест получает свежие драйвер/сессию.
- **Покрытие** — позитивные, негативные и сценарные кейсы; проверка статус-кодов и тела ответа.
