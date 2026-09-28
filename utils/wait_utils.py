from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_element(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )

def wait_for_elements(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_all_elements_located(locator)
    )
