from selenium.webdriver.common.by import By

class MenuComponent:
    LOGOUT = (By.LINK_TEXT, "Logout")
    LOGIN = (By.LINK_TEXT, 'Login')
    SIGNUP = (By.LINK_TEXT, "Sign Up")
    RESONA_SHOES = (By.LINK_TEXT, "RESONA SHOES")
    HOME = (By.LINK_TEXT, "Home")
    CART = (By.XPATH, '//*[@id="mainNav"]/ul[1]/li[2]/a')

    def __init__(self, driver):
        self.driver = driver

    def logout(self):
        self.driver.find_element(*self.LOGOUT).click()

    def login(self):
        self.driver.find_element(*self.LOGIN).click()

    def signup(self):
        self.driver.find_element(*self.SIGNUP).click()

    def resona_shoes(self):
        self.driver.find_element(*self.RESONA_SHOES).click()

    def home(self):
        self.driver.find_element(*self.HOME).click()

    def cart(self):
        self.driver.find_element(*self.CART).click()
