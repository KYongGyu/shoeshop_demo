from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ItemDetailPage:
    CART_ADD_BTN = (By.CSS_SELECTOR, ".btn-primary")
    GO_TO_CART_BTN = (By.CSS_SELECTOR, ".btn-outline-secondary")
    GO_TO_MAIN_BTN = (By.CSS_SELECTOR, "a.btn-link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_page(self, url):
        self.driver.get(url)
        return self

    def click(self, locator):
        el = self.wait.until(EC.element_to_be_clickable(locator))
        el.click()
        return el

    def add_item(self):
        add_btn = self.driver.find_element(*self.CART_ADD_BTN)
        add_btn.click()

    def go_to_cart(self):
        go_to_cart_btn = self.driver.find_element(*self.GO_TO_CART_BTN)
        go_to_cart_btn.click()

    def go_to_main(self):
        go_to_main_btn = self.driver.find_element(*self.GO_TO_MAIN_BTN)
        go_to_main_btn.click()
