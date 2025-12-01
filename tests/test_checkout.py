# def_go_checkout(inv):
#     inv.add_item(inv.item_names()[0])
#     inv.wait_cart_count(1)
#     inv.go_cart()
#     CartPage(inv.driver).checkout()
#     return CheckoutPage(inv.driver)
from time import sleep

from selenium.webdriver.common.by import By
import time

from tests.pages.checkout_page import CheckoutPage


# @pytest.mark.negative
# def test_checkout_required_first_name(login_standard):
#     chk=_go_checkout()

def test_blank_name_input_checkout_page(browser):
    #로그인과정

    browser.get("http://127.0.0.1:5000/")
    menu_login = browser.find_element(By.LINK_TEXT, "Login")

    menu_login.click()
    browser.find_element(By.ID, "username").send_keys("test-user")
    browser.find_element(By.ID, "password").send_keys("1234")
    browser.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    sleep(5)

    #장바구니에 물건 넣기
    browser.get("http://127.0.0.1:5000/product/4")
    sleep(5)
    browser.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    sleep(5)

    #결제페이지
    browser.get("http://127.0.0.1:5000/checkout")
    sleep(5)
    checkout_page = CheckoutPage(browser)
    checkout_page.enter_phone_number("010-2027-6120")
    checkout_page.enter_address("비전동")

    checkout_page.click_submit_btn()
    sleep(5)

    alert_window = browser.find_element(By.CSS_SELECTOR, ".alert-danger")

    assert "모든 필수 정보를 입력해주세요." == alert_window.text

def test_blank_phone_number_input_checkout_page(browser):

    browser.get("http://127.0.0.1:5000/checkout")
    menu_login = browser.find_element(By.LINK_TEXT, "Login")

    menu_login.click()
    browser.find_element(By.ID, "username").send_keys("test-user")
    browser.find_element(By.ID, "password").send_keys("1234")
    sleep(5)
    browser.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    sleep(5)

    # 장바구니에 물건 넣기
    browser.get("http://127.0.0.1:5000/product/4")
    sleep(5)
    browser.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    sleep(5)

    # 결제페이지
    browser.get("http://127.0.0.1:5000/checkout")
    sleep(5)
    checkout_page = CheckoutPage(browser)
    checkout_page.enter_username("user1")
    checkout_page.enter_phone_number("")
    checkout_page.enter_address("비전동")

    checkout_page.click_submit_btn()
    sleep(5)

    alert_window = browser.find_element(By.CSS_SELECTOR, ".alert-danger")

    assert "모든 필수 정보를 입력해주세요." == alert_window.text

def test_blank_address_input_checkout_page(browser):
    browser.get("http://127.0.0.1:5000/checkout")
    menu_login = browser.find_element(By.LINK_TEXT, "Login")

    menu_login.click()
    browser.find_element(By.ID, "username").send_keys("test-user")
    browser.find_element(By.ID, "password").send_keys("1234")
    sleep(5)
    browser.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    sleep(5)

    # 장바구니에 물건 넣기
    browser.get("http://127.0.0.1:5000/product/4")
    sleep(5)
    browser.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    sleep(5)

    # 결제페이지
    browser.get("http://127.0.0.1:5000/checkout")
    sleep(5)
    checkout_page = CheckoutPage(browser)
    checkout_page.enter_username("user1")
    checkout_page.enter_phone_number("010-8572-0931")
    checkout_page.enter_address("")

    checkout_page.click_submit_btn()
    sleep(5)

    alert_window = browser.find_element(By.CSS_SELECTOR, ".alert-danger")

    assert "모든 필수 정보를 입력해주세요." == alert_window.text