from time import sleep

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.pages.cart_page import CartPage
from tests.pages.inventory_page import InventoryPage
from tests.test_signup import base_url
from utils.auth import clean_session, user_login

BASE_URL = "http://127.0.0.1:5000"

@pytest.mark.smoke
def test_add_remove_cart_from_inventory(browser):
    # 로그인된 상태로, 장바구니에서 상품을 추가하고 제거하여 장바구니 카운트를 검증
    clean_session(browser)
    user_login(browser)

    inventory_page = InventoryPage(browser)

    inventory_page.add_item("Air Runner 1")
    sleep(5)
    inventory_page.add_item("Street Walker")
    sleep(5)

    browser.get(BASE_URL + "/cart")
    sleep(5)
    before_remove_items_count = len(browser.find_elements(By.XPATH, "//table/tbody/tr"))
    browser.find_element(By.XPATH, "/html/body/main/div[1]/table/tbody/tr[1]/td[5]/form/button").click()

    sleep(5)

    after_remove_items_count = len(browser.find_elements(By.XPATH, "//table/tbody/tr"))
    sleep(5)

    assert before_remove_items_count - 1 == after_remove_items_count


@pytest.mark.regression
def test_remove_item_in_cart_page(browser):
    clean_session(browser)
    user_login(browser)

    inventory_page = InventoryPage(browser)

    # 장바구니에서 상품을 제거하고, 상품이 제거되었는지 검증
    inventory_page.add_item("Air Runner 1")
    sleep(5)
    browser.get(BASE_URL + "/cart")
    before_remove_items_count = len(browser.find_elements(By.XPATH, "//table/tbody/tr"))
    assert before_remove_items_count == 1 # 장바구니에 1개의 아이템이 있는지 확인


    browser.find_element(By.XPATH, "/html/body/main/div[1]/table/tbody/tr[1]/td[5]/form/button").click()
    sleep(5)
    after_remove_items_count = len(browser.find_elements(By.XPATH, "//table/tbody/tr"))
    assert after_remove_items_count == 0 # 장바구니가 비어 있는지 확인

@pytest.mark.smoke
def test_total_math(browser):
    clean_session(browser)
    user_login(browser)

    inventory_page = InventoryPage(browser)

    inventory_page.add_item("Air Runner 1")
    sleep(5)
    inventory_page.add_item("Street Walker")
    sleep(5)

    # 장바구니의 총 금액이 올바르게 계산되었는지 검증
    browser.get(BASE_URL + "/cart")
    sleep(5)
    cart = browser.find_elements(By.XPATH, "//table/tbody/tr")
    expected_tot_price = 0

    for i in range(1, len(cart) + 1):
        price_text = browser.find_element(By.XPATH, "/html/body/main/div[1]/table/tbody/tr[%d]/td[4]" %i).text
        temp_price_text = price_text.replace(",", "")
        price = int(temp_price_text.replace("원", ""))
        expected_tot_price = expected_tot_price + price # 각 아이템의 가격을 총합에 더함

    tot_price_text = browser.find_element(By.XPATH, "/html/body/main/div[1]/table/tfoot/tr/th[2]").text
    temp_tot_price_text = tot_price_text.replace(",", "")
    tot_price = int(temp_tot_price_text.replace("원", ""))

    print(expected_tot_price, tot_price)

    assert expected_tot_price == tot_price #계산된 총액과 실제 금액이 일치하는지 확인

@pytest.mark.regression
def test_continue_shopping_returns_inventory(browser):
    # 쇼핑 계속하기 버튼을 눌러 인벤토리 페이지로 돌아가는지 확인
    browser.get(BASE_URL + "/cart")
    sleep(5)
    browser.find_element(By.LINK_TEXT, "쇼핑 계속하기").click()
    sleep(5)

    assert BASE_URL in browser.current_url # 인벤토리 페이지로 돌아갔는지 확인

def test_go_checkout(browser):
    # 결제 페이지로 이동하여, 결제 버튼 클릭 후 URL 확인
    clean_session(browser)
    user_login(browser)

    inventory_page = InventoryPage(browser)

    inventory_page.add_item("Air Runner 1")
    sleep(5)
    inventory_page.add_item("Street Walker")
    sleep(5)

    browser.get(BASE_URL + "/cart")
    sleep(5)

    browser.find_element(By.CSS_SELECTOR, ".btn-success").click()

    sleep(5)

    assert BASE_URL + "/checkout" in browser.current_url
