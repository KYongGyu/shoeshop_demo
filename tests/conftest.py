import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def browser():
    options = webdriver.ChromeOptions()
    # options.add_argument("headless")

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_leak_detection": False
    }
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)
    # driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()