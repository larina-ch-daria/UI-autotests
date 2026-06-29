# SauceDemo UI Tests

UI-автотесты для тренировочного сайта [saucedemo.com](https://www.saucedemo.com/).

**Стек:** Python, Selenium, pytest
**Архитектура:** Page Object Model (POM)

## Что покрыто

| Тест | Тип | Проверка |
|------|-----|----------|
| `test_successful_login` | позитивный | вход с валидными данными → страница товаров |
| `test_login_with_wrong_password` | негативный | неверный пароль → сообщение об ошибке |
| `test_locked_out_user` | негативный | заблокированный пользователь → ошибка блокировки |
| `test_add_item_to_cart` | сценарий | вход → добавление товара → счётчик корзины = 1 |

## Структура

```
saucedemo-tests/
├── pages/                 # Page Object — классы страниц
│   ├── base_page.py       # базовый класс: общие методы + явные ожидания (WebDriverWait)
│   ├── login_page.py      # страница логина: локаторы + действия
│   └── inventory_page.py  # страница товаров после входа
├── tests/
│   └── test_login.py      # тест-кейсы
├── conftest.py            # фикстура драйвера (setup/teardown через yield)
├── requirements.txt
└── README.md
```

## Запуск

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
pytest -v
```

Selenium 4 сам подтягивает драйвер браузера через встроенный Selenium Manager — отдельно ставить chromedriver не нужно.

## Технические решения

- **Page Object Model** — каждая страница описана отдельным классом, локаторы хранятся внутри класса, а не в тестах. При изменении вёрстки правка в одном месте.
- **Явные ожидания** (`WebDriverWait` + `expected_conditions`) вместо `time.sleep()` — ждём ровно до выполнения условия, а не фиксированное время.
- **Фикстура драйвера** в `conftest.py` через `yield`: setup до, teardown (`driver.quit()`) после — закрытие браузера срабатывает даже при падении теста.
- **Изоляция тестов** — каждый тест получает свежий драйвер, тесты независимы.
