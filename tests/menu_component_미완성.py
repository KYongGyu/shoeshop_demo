from selenium.webdriver.common.by import By
from saucedemo.pages.base_page import BasePage

class MenuComponent(BasePage):
    MENU_BTN = (By.ID, "react-burger-menu-btn")
    CLOSE_BTN = (By.ID, "react-burger-cross-btn")
    LOGOUT = (By.ID, "logout_topbar_link")

    def open_menu(self):
        self.c(self.MENU_BTN)

    def close_menu(self):
        self.c(self.CLOSE_BTN)

    def logout(self):
        self.c(self.LOGOUT)
