from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username = (By.ID, "user-name")
        self.password = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message = (By.CSS_SELECTOR, ".error-message-container")

    def login(self, user, pwd):
        self.type(self.username, user)
        self.type(self.password, pwd)
        self.click(self.login_button)

    def get_error(self):
        return self.get_text(self.error_message)
