from selenium import webdriver

def get_driver():
    options = webdriver.ChromeOptions()
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
