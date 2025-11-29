from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ItemDetailPage:
    def __init__(self, driver):
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

    def goto(self, url):
        self.driver.get(url)