import pytest
from selenium.webdriver.common.by import By
from utils.driver_setup import get_driver
from pages.login_page import LoginPage

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

# Happy Path
def test_standard_user_login(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    assert "inventory.html" in driver.current_url, "Standard user should reach inventory page"

# Negative Scenario
def test_invalid_credentials(driver):
    login_page = LoginPage(driver)
    login_page.login("invalid_user", "wrong_pass")
    assert "Username and password do not match" in login_page.get_error(), "Invalid credentials should show error"

#  Negative Scenario
def test_empty_fields(driver):
    login_page = LoginPage(driver)
    login_page.login("", "")
    error = login_page.get_error()
    assert "Username is required" in error or "Password is required" in error, "Empty fields should trigger validation"

# Edge Case
def test_locked_out_user(driver):
    login_page = LoginPage(driver)
    login_page.login("locked_out_user", "secret_sauce")
    assert "locked out" in login_page.get_error().lower(), "Locked out user should see locked message"

# Edge Case
def test_problem_user(driver):
    login_page = LoginPage(driver)
    login_page.login("problem_user", "secret_sauce")
    assert "inventory.html" in driver.current_url, "Problem user should still log in"
    images = driver.find_elements(By.CLASS_NAME, "inventory_item_img")
    assert len(images) > 0, "Problem user should see inventory items even if images are broken"

# Edge Case
def test_performance_glitch_user(driver):
    login_page = LoginPage(driver)
    login_page.login("performance_glitch_user", "secret_sauce")
    assert "inventory.html" in driver.current_url, "Performance glitch user should eventually reach inventory page"

# Edge Case
def test_visual_user(driver):
    login_page = LoginPage(driver)
    login_page.login("visual_user", "secret_sauce")
    assert "inventory.html" in driver.current_url, "Visual user should reach inventory page"
