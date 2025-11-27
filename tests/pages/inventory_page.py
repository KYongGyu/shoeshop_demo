from selenium.webdriver.common.by import By
import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    DEFAULT_TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", "15"))

    ITEM_CARDS = (By.CSS_SELECTOR, ".card")
    DETAIL_BTN = (By.CSS_SELECTOR, ".card a.btn-outline-secondary")
    CART_ADD_BTN = (By.CSS_SELECTOR, ".btn-primary")
    CART_REMOVE_BTN = (By.CSS_SELECTOR, ".btn-warning")

    def __init__(self, driver, base_url):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        self.driver.get(url)
        return self

    def click(self, locator):
        el = self.wait.until(EC.element_to_be_clickable(locator))
        el.click()
        return el

    def text_present(self, text):
        return text in self.driver.page_source

    def get_elements(self, locator):
        self.wait.until(EC.presence_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    def item_cards(self):
        return self.driver.find_elements(*self.ITEM_CARDS)

    def _find_card(self, name):
        for c in self.item_cards():
            if name in c.text:
                return c
        raise AssertionError(f"Item not found: {name}")

    def open_detail(self, name):
        card = self._find_card(name)
        btn = card.find_element(*self.DETAIL_BTN)
        if "카트에 담기" in btn.text:
            try:
                self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", btn)
                btn.click()
            except Exception:
                self.driver.execute_script("arguments[0].click();", btn)

    def add_item(self, name):
        card = self._find_card(name)
        btn = card.find_element(*self.CART_ADD_BTN)
        try:
            self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", btn)
            btn.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", btn)

    def remove_item(self, name):
        card = self._find_card(name)
        btn = card.find_element(*self.CART_REMOVE_BTN)
        try:
            self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", btn)
            btn.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", btn)