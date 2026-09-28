import pytest
from selenium.webdriver.common.by import By
from utils.driver_setup import get_driver
from utils.wait_utils import wait_for_elements, wait_for_element
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def test_inventory_products(driver):
    LoginPage(driver).login("standard_user", "secret_sauce")
    inventory = InventoryPage(driver)
    names = wait_for_elements(driver, (By.CLASS_NAME, "inventory_item_name"))
    prices = wait_for_elements(driver, (By.CLASS_NAME, "inventory_item_price"))
    assert len(names) > 0, "Product list should not be empty"
    assert len(names) == len(prices), "Each product should have a price"

def test_add_to_cart(driver):
    LoginPage(driver).login("standard_user", "secret_sauce")
    inventory = InventoryPage(driver)
    inventory.add_product_to_cart("Sauce Labs Backpack")
    cart_badge = wait_for_element(driver, (By.CLASS_NAME, "shopping_cart_badge")).text
    assert cart_badge == "1", "Cart badge should show 1 item added"
