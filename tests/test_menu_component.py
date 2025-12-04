from time import sleep

from selenium.webdriver.common.by import By

from tests.pages.menu_component import MenuComponent
from utils.auth import clean_session, user_login

BASE_URL = 'http://127.0.0.1:5000'

def test_login_in_menu_component(browser):
    clean_session(browser)

    menu_component = MenuComponent(browser)

    menu_component.login()
    sleep(5)

    assert BASE_URL + '/login' == browser.current_url

def test_logout_in_menu_component(browser):
    clean_session(browser)
    user_login(browser)

    menu_component = MenuComponent(browser)
    menu_component.logout()

    sleep(5)
    alert_window = browser.find_element(By.CSS_SELECTOR, ".alert-info")

    assert "로그아웃되었습니다." == alert_window.text

def test_signup_in_menu_component(browser):
    clean_session(browser)

    menu_component = MenuComponent(browser)
    menu_component.signup()

    sleep(5)

    assert BASE_URL + '/register' == browser.current_url


def test_go_to_home_in_menu_component(browser):
    browser.get(BASE_URL + '/product/9')

    menu_component = MenuComponent(browser)
    menu_component.home()

    sleep(5)

    assert BASE_URL + "/" == browser.current_url


def test_go_to_resona_shop_in_menu_component(browser):
    browser.get(BASE_URL + '/product/1')

    menu_component = MenuComponent(browser)
    menu_component.resona_shoes()

    sleep(5)

    assert BASE_URL + "/"  == browser.current_url

def test_go_to_cart_in_menu_component(browser):
    browser.get(BASE_URL)

    menu_component = MenuComponent(browser)

    menu_component.cart()

    sleep(5)

    assert BASE_URL + "/cart" == browser.current_url

