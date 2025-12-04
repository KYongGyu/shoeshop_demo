from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.ID, "name").send_keys(username)

    def enter_phone_number(self, phone_number):
        self.driver.find_element(By.ID, "phone").send_keys(phone_number)

    def enter_address(self, address):
        self.driver.find_element(By.ID, "address").send_keys(address)

    def click_submit_btn(self):
        self.driver.find_element(By.CSS_SELECTOR, ".btn-success").click()