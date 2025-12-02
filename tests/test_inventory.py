from time import sleep

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.pages.inventory_page import InventoryPage
from utils.auth import clean_session, user_login

BASE_URL = "http://127.0.0.1:5000"


@pytest.mark.regression
def test_open_detail_page(browser):

    inventory_page = InventoryPage(browser)
    item_name = "Trail Hiker"

    inventory_page.open_page(BASE_URL)
    inventory_page.open_detail(item_name)

    assert item_name in browser.title

@pytest.mark.regression
def test_login_user_add_cart_in_inventory_page(browser):
    clean_session(browser)
    user_login(browser)

    inventory_page = InventoryPage(browser)
    inventory_page.open_page(BASE_URL)

    WebDriverWait(browser, 10).until(EC.url_to_be(BASE_URL + "/"))
    item_name = "Canvas Breeze"

    inventory_page.add_item(item_name)
    sleep(5)

    alert_success_window = browser.find_element(By.CSS_SELECTOR, ".alert-success")

    assert "장바구니에 추가되었습니다." in alert_success_window.text


@pytest.mark.regression
def test_logout_user_add_cart_in_inventory_page(browser):
    clean_session(browser)

    inventory_page = InventoryPage(browser)
    item_name = "Canvas Breeze"

    inventory_page.open_page(BASE_URL)

    inventory_page.add_item(item_name)
    sleep(5)

    print(browser.title)

    assert "Login" in browser.title

@pytest.mark.regression
def test_login_user_remove_cart_in_inventory_page(browser):
    clean_session(browser)
    user_login(browser)

    inventory_page = InventoryPage(browser)
    inventory_page.open_page(BASE_URL)

    WebDriverWait(browser, 10).until(EC.url_to_be(BASE_URL + "/"))
    item_name = "Canvas Breeze"

    inventory_page.add_item(item_name)
    sleep(5)

    inventory_page.remove_item(item_name)

    alert_success_window = browser.find_element(By.CSS_SELECTOR, ".alert-info")

    assert "장바구니에서 제거되었습니다." in alert_success_window.text




