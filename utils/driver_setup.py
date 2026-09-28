import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_driver():
    options = Options()

    # Detect if running in CI (GitHub Actions sets CI=true)
    if os.getenv("CI"):
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
    else:
        options.add_argument("--start-maximized")

    # Disable password save prompt
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.saucedemo.com/")
    return driver
