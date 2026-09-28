from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.zip_code = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.finish_button = (By.ID, "finish")
        self.success_message = (By.CLASS_NAME, "complete-header")
        self.error_message = (By.CSS_SELECTOR, ".error-message-container")

    def fill_checkout_info(self, fname, lname, zip_code):
        # ✅ Wait for fields before typing
        self.type(self.first_name, fname)
        self.type(self.last_name, lname)
        self.type(self.zip_code, zip_code)
        self.click(self.continue_button)

    def finish_checkout(self):
        self.click(self.finish_button)

    def get_success_message(self):
        return self.get_text(self.success_message)

    def get_error_message(self):
        return self.get_text(self.error_message)
