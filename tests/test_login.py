from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_successful_login(driver):
    """Позитивный: валидные данные → попадаем на страницу товаров."""
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    assert inventory.get_title() == "Products"
    assert "inventory" in driver.current_url


def test_login_with_wrong_password(driver):
    """Негативный: неверный пароль → сообщение об ошибке."""
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "wrong_password")

    error = login_page.get_error()
    assert "Username and password do not match" in error


def test_locked_out_user(driver):
    """Негативный: заблокированный пользователь → ошибка блокировки."""
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("locked_out_user", "secret_sauce")

    error = login_page.get_error()
    assert "locked out" in error


def test_add_item_to_cart(driver):
    """Сценарий: вход → добавление товара → счётчик корзины = 1."""
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    inventory.add_backpack_to_cart()
    assert inventory.get_cart_count() == "1"
