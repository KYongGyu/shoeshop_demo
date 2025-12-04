from selenium.webdriver.common.by import By

class SignupPage:
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    CONFIRM_PASSWORD = (By.NAME, "confirm_password")
    SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")
    BASE_URL = "http://127.0.0.1:5000"

    def __init__(self, driver):
        self.driver = driver

    def open_signup(self):
        return self.driver.get(self.BASE_URL + "/signup")

    def signup(self, username, password,confirm_password=None):
        if confirm_password is None:
            confirm_password = password
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.type(self.CONFIRM_PASSWORD, confirm_password)
        self.click(self.SUBMIT)


