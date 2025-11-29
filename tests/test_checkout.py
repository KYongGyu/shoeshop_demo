from selenium import webdriver
from selenium. webdriver.common.by import by
from selenium. webdriver.support.wait import WebDriverWait
from selinium.webdriver.support import expected_conditions as expected_conditions

driver = webdriver.Firefox()
driver.get("http://somedomain/url_that_delays_loading")
try:
    element = WebDriverWait(driver, 10).until(
        E
    )