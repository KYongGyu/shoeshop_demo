from time import sleep

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.pages.item_detail_page import ItemDetailPage
from utils.auth import clean_session, user_login

BASE_URL = "http://127.0.0.1:5000"


@pytest.mark.smoke
def test_logout_user_add_cart_in_item_detail_page(browser):
    clean_session(browser)

    item_detail_page = ItemDetailPage(browser)
    product_path = "/product/7"
    item_detail_page.open_page(BASE_URL + product_path)
    WebDriverWait(browser, 5).until(EC.url_to_be(BASE_URL + product_path))

    item_detail_page.add_item()

    alert_require_login_window = browser.find_element(By.CSS_SELECTOR, ".alert-warning")

    assert "로그인이 필요합니다." in alert_require_login_window.text

@pytest.mark.smoke
def test_login_user_add_cart_in_item_detail_page(browser):
    clean_session(browser)
    user_login(browser)

    item_detail_page = ItemDetailPage(browser)

    product_path = "/product/7"
    item_detail_page.open_page(BASE_URL + product_path)
    WebDriverWait(browser, 5).until(EC.url_to_be(BASE_URL + product_path))

    item_detail_page.add_item()

    alert_cart_add_success_window = browser.find_element(By.CSS_SELECTOR, ".alert-success")

    assert "장바구니에 추가되었습니다." in alert_cart_add_success_window.text

@pytest.mark.xfail
def test_logout_user_go_to_cart_in_item_detail_page(browser):
    clean_session(browser)
    item_detail_page = ItemDetailPage(browser)
    product_path = "/product/7"
    item_detail_page.open_page(BASE_URL + product_path)
    WebDriverWait(browser, 5).until(EC.url_to_be(BASE_URL + product_path))

    item_detail_page.go_to_cart()

    WebDriverWait(browser, 5).until(EC.url_to_be(BASE_URL))

    assert "Home" in browser.title

@pytest.mark.smoke
def test_login_user_remove_cart_in_item_detail_page(browser):
    clean_session(browser)
    user_login(browser)

    item_detail_page = ItemDetailPage(browser)

    product_path = "/product/7"
    item_detail_page.open_page(BASE_URL + product_path)
    WebDriverWait(browser, 5).until(EC.url_to_be(BASE_URL + product_path))

    item_detail_page.go_to_cart()

    assert "Cart" in browser.title

@pytest.mark.smoke
def test_go_to_main_in_item_detail_page(browser):
    item_detail_page = ItemDetailPage(browser)
    product_path = "/product/7"
    item_detail_page.open_page(BASE_URL + product_path)
    WebDriverWait(browser, 5).until(EC.url_to_be(BASE_URL + product_path))

    item_detail_page.go_to_main()

    assert "Home" in browser.title