from time import sleep

import pytest
from selenium.webdriver.common.by import By

from tests.pages.item_detail_page import ItemDetailPage

BASE_URL = "http://127.0.0.1:5000"


@pytest.mark.regression
def test_logout_user_add_cart_in_item_detail_page(browser):
    item_detail_page = ItemDetailPage(browser)
    product_path = "/product/7"
    item_detail_page.open_page(BASE_URL + product_path)
    sleep(5)

    item_detail_page.add_item()

    alert_require_login_window = browser.find_element(By.CSS_SELECTOR, ".alert-warning")

    assert "로그인이 필요합니다." in alert_require_login_window.text

@pytest.mark.regression
def test_login_user_add_cart_in_item_detail_page(browser):
    # 로그인 과정
    item_detail_page = ItemDetailPage(browser)
    item_detail_page.open_page(BASE_URL)
    sleep(5)

    menu_login = browser.find_element(By.LINK_TEXT, "Login")

    menu_login.click()
    browser.find_element(By.ID, "username").send_keys("test-user")
    browser.find_element(By.ID, "password").send_keys("1234")
    browser.find_element(By.CSS_SELECTOR, ".btn-primary").click()

    product_path = "/product/7"
    item_detail_page.open_page(BASE_URL + product_path)
    sleep(5)

    item_detail_page.add_item()

    alert_cart_add_success_window = browser.find_element(By.CSS_SELECTOR, ".alert-success")

    assert "장바구니에 추가되었습니다." in alert_cart_add_success_window.text

@pytest.mark.regression
def test_logout_user_go_to_cart_in_item_detail_page(browser):
    item_detail_page = ItemDetailPage(browser)
    product_path = "/product/7"
    item_detail_page.open_page(BASE_URL + product_path)
    sleep(5)

    item_detail_page.go_to_cart()

    sleep(5)

    assert "Home" in browser.title

@pytest.mark.regression
def test_login_user_remove_cart_in_item_detail_page(browser):
    # 로그인 과정
    item_detail_page = ItemDetailPage(browser)
    item_detail_page.open_page(BASE_URL)
    sleep(5)

    menu_login = browser.find_element(By.LINK_TEXT, "Login")

    menu_login.click()
    browser.find_element(By.ID, "username").send_keys("test-user")
    browser.find_element(By.ID, "password").send_keys("1234")
    browser.find_element(By.CSS_SELECTOR, ".btn-primary").click()

    product_path = "/product/7"
    item_detail_page.open_page(BASE_URL + product_path)
    sleep(5)

    item_detail_page.go_to_cart()

    assert "Cart" in browser.title

@pytest.mark.regression
def test_go_to_main_in_item_detail_page(browser):
    item_detail_page = ItemDetailPage(browser)
    product_path = "/product/7"
    item_detail_page.open_page(BASE_URL + product_path)
    sleep(5)

    item_detail_page.go_to_main()
    sleep(5)

    assert "Home" in browser.title