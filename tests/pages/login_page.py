from selenium.webdriver.common.by import By

class LoginPage:
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")

    BASE_URL = "http://127.0.0.1:5000"

    def __init__(self, driver):
        self.driver = driver

    def open_login(self):
        return self.driver.get(self.BASE_URL + "/login")

    def login(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
