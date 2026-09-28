from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.checkout_button = (By.ID, "checkout")
        self.continue_shopping_button = (By.ID, "continue-shopping")
        self.remove_button = (By.CLASS_NAME, "cart_button")

    def proceed_to_checkout(self):
        self.click(self.checkout_button)

    def remove_item(self):
        self.click(self.remove_button)

    def continue_shopping(self):
        self.click(self.continue_shopping_button)
