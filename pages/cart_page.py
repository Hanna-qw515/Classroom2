# pages/cart_page.py
import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
        ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
        ITEM_PRICES = (By.CLASS_NAME, "inventory_item_price")
        CHECKOUT_BUTTON = (By.ID, "checkout")
        def get_item_names(self):
            return self.get_texts(self.ITEM_NAMES)

        def get_item_prices(self):
            return [float(p.replace("$", "")) for p in self.get_texts(self.ITEM_PRICES)]
        def checkout(self):
            self.click(self.CHECKOUT_BUTTON)
            from pages.checkout_pages import CheckoutInfoPage
            return CheckoutInfoPage(self.driver)