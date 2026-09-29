import pytest
from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def test_checkout_success(driver):
    LoginPage(driver).login("standard_user", "secret_sauce")
    inv = InventoryPage(driver)
    inv.add_product_to_cart("Sauce Labs Bike Light")
    inv.go_to_cart()
    cart = CartPage(driver)
    cart.proceed_to_checkout()
    checkout = CheckoutPage(driver)
    checkout.fill_checkout_info("Binay", "Thapa", "44600")
    checkout.finish_checkout()

    # Normalize case to avoid mismatch
    msg = checkout.get_success_message()
    assert "thank you for your order" in msg.lower()

def test_checkout_missing_info(driver):
    LoginPage(driver).login("standard_user", "secret_sauce")
    inv = InventoryPage(driver)
    inv.add_product_to_cart("Sauce Labs Bike Light")
    inv.go_to_cart()
    cart = CartPage(driver)
    cart.proceed_to_checkout()
    checkout = CheckoutPage(driver)
    checkout.click(checkout.continue_button)

    error = checkout.get_error_message()
    assert "error" in error.lower() or "required" in error.lower()
