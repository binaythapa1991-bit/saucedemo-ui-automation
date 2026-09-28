from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage

class InventoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.cart_icon = (By.ID, "shopping_cart_container")
        self.sort_dropdown = (By.CLASS_NAME, "product_sort_container")
        self.product_names = (By.CLASS_NAME, "inventory_item_name")
        self.product_prices = (By.CLASS_NAME, "inventory_item_price")
        self.add_buttons = (By.CLASS_NAME, "btn_inventory")

    def add_product_to_cart(self, product_name):
        names = self.wait_for_elements(self.product_names)
        buttons = self.driver.find_elements(*self.add_buttons)
        for i, name in enumerate(names):
            if name.text == product_name:
                buttons[i].click()
                break

    def go_to_cart(self):
        self.click(self.cart_icon)

    def sort_products(self, option_text):
        Select(self.wait_for_element(self.sort_dropdown)).select_by_visible_text(option_text)

    def get_all_product_names(self):
        return [el.text for el in self.wait_for_elements(self.product_names)]

    def get_all_product_prices(self):
        return [el.text for el in self.wait_for_elements(self.product_prices)]
