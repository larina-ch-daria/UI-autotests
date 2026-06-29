import pytest
import requests
from selenium import webdriver


API_BASE_URL = "https://restful-booker.herokuapp.com"


@pytest.fixture
def base_url():
    return API_BASE_URL


@pytest.fixture
def api_session():
    session = requests.Session()
    session.headers.update({"Content-Type": "application/json"})
    yield session            # setup до yield, тесты используют сессию, teardown после
    session.close()          # teardown: закрываем сессию


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless=new")  # включить, чтобы гонять без окна браузера
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)        # неявное ожидание: до 5 сек ждём появления элемента
    driver.maximize_window()

    yield driver                     # setup до yield, тест получает драйвер, teardown после

    driver.quit()                    # teardown: закрываем браузер после каждого теста
