from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):
    TITLE = (By.CLASS_NAME, "title")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")

    def get_title(self):
        return self.find(self.TITLE).text

    def add_backpack_to_cart(self):
        self.click(self.ADD_BACKPACK)

    def get_cart_count(self):
        return self.find(self.CART_BADGE).text
