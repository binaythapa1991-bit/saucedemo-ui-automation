import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_driver():
    options = Options()

    # Headless only in CI
    if os.getenv("CI"):
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
    else:
        options.add_argument("--start-maximized")

    # Launch Chrome in incognito with a clean profile
    options.add_argument("--incognito")
    options.add_argument("--user-data-dir=/tmp/chrome-profile")

    # Disable password manager and safety checks
    options.add_argument("--disable-features=PasswordManagerOnboarding,PasswordCheck,SafeBrowsingEnhancedProtection")
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-notifications")

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.default_content_setting_values.notifications": 2
    }
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.saucedemo.com/")
    return driver

@pytest.fixture
def driver():
    drv = get_driver()
    yield drv
    drv.quit()
