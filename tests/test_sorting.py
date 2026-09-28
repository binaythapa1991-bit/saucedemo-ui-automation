import pytest
from selenium.webdriver.common.by import By
from utils.driver_setup import get_driver
from utils.wait_utils import wait_for_elements
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def test_sort_products(driver):
    LoginPage(driver).login("standard_user", "secret_sauce")
    inv = InventoryPage(driver)
    inv.sort_products("Price (low to high)")
    prices = [float(el.text.replace("$", "")) for el in wait_for_elements(driver, (By.CLASS_NAME, "inventory_item_price"))]
    assert prices == sorted(prices), "Products should be sorted by price low to high"
