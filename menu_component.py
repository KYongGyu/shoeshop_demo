from selenium.webdriver.common.by import By
from saucedemo.pages.base_page import BasePage

class MenuComponent(BasePage):

    LOGOUT = (By.ID, "logout_topbar_link")
    LOGIN = (By.ID, "login_topbar_link")
    SIGNUP = (By.ID, "signup_topbar_link")


    def logout(self):
        if self.is_logged_in():
            self.c(self.LOGOUT)

    def login(self):
        if self.is_logged_out():
            self.c(self.LOGIN)

    def signup(self):
        if self.is_logged_out():
            self.c(self.SIGNUP)

    def is_logged_in(self):
        return self.is_element_present(self.LOGOUT)

    def is_logged_out(self):
        return self.is_element_present(self.LOGIN) and self.is_element_present(self.SIGNUP)