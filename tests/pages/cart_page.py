from selenium.webdriver.common.by import By
import re
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage():
    ITEMS = (By.CSS_SELECTOR, ".cart_item")
    ITEM_NAME = (By.CSS_SELECTOR, ".inventory_item_name")
    REMOVE_BTN = (By.CSS_SELECTOR, "button.cart_button")
    ITEM_TOTAL = (By.CSS_SELECTOR, "summary_subtotal_label")
    CONTINUE_SHOP = (By.ID, "continue-shopping")
    CHECKOUT = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver

    def items(self):
        return self.driver.find_elements(*self.ITEMS)
        if not items:
            raise AssertionError("장바구니가 비어 있습니다.")
        return items

    def item_name(self):
        return [i.find_element(*self.ITEM_NAME).text for i in self.items()]

    def remove(self, name):
        for i in self.items():
            if name in i.text:
                btn = i.find_element(*self.REMOVE_BTN)
                try:
                    btn.click()
                except Exception:
                    self.driver.execute_script("arguments[0].click();", btn)
                return
        raise AssertionError(f"장바구니에서 제거되었습니다.: {name}")

    def _money(self, locator):
        txt = self.v(locator).text
        amount = re.sub(r"[^\d.]", "", txt)
        return float(amount)

    def item_total(self):
        return self._money(self.ITEM_TOTAL)

    def continue_shopping(self):
        self.c(self.CONTINUE_SHOP)
        self.url_contains("inventory")

    def checkout(self):
        self.c(self.CHECKOUT)
        self.url_contains("checkout")

    def v(self, locator):
        return self.driver.find_element(*locator)

    def c(self, locator):
        self.driver.find_element(*locator).click()

    def url_contains(self, substring):
        return substring in self.driver.current_url