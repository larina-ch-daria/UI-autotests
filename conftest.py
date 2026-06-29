import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless=new")  # включить, чтобы гонять без окна браузера
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)        # неявное ожидание: до 5 сек ждём появления элемента
    driver.maximize_window()

    yield driver                     # setup до yield, тест получает драйвер, teardown после

    driver.quit()                    # teardown: закрываем браузер после каждого теста
