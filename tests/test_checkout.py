from time import sleep

from selenium.webdriver.common.by import By

from tests.pages.checkout_page import CheckoutPage
from utils.auth import clean_session


def test_blank_name_input_checkout_page(browser):
    #로그인과정
    clean_session(browser)
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
    checkout_page.enter_phone_number("010-2030-6120")
    checkout_page.enter_address("비전동")

    checkout_page.click_submit_btn()
    sleep(5)

    alert_window = browser.find_element(By.CSS_SELECTOR, ".alert-danger")

    assert "모든 필수 정보를 입력해주세요." == alert_window.text.strip()

def test_blank_phone_number_input_checkout_page(browser):
    clean_session(browser)

    browser.get("http://127.0.0.1:5000")
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

    assert "모든 필수 정보를 입력해주세요." == alert_window.text.strip()

def test_blank_address_input_checkout_page(browser):
    clean_session(browser)

    browser.get("http://127.0.0.1:5000")
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

    assert "모든 필수 정보를 입력해주세요." == alert_window.text.strip()

def test_go_to_success_page(browser):
    clean_session(browser)

    browser.get("http://127.0.0.1:5000")
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
    checkout_page.enter_username("문성식")
    checkout_page.enter_phone_number("010-8572-0931")
    checkout_page.enter_address("용이동")

    success = browser.find_element(By.CSS_SELECTOR, ".btn.btn-success")
    success.click()
    sleep(5)

    alert_window = browser.find_element(By.CSS_SELECTOR, ".alert.alert-success.mb-2")

    assert "결제가 완료되었습니다! 주문이 접수되었습니다." == alert_window.text.strip()


def test_go_to_cart_page(browser):
    clean_session(browser)
    browser.get("http://127.0.0.1:5000")
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

    alert_window = browser.find_element(By.CSS_SELECTOR, ".alert-success")

    # 결제페이지
    browser.get("http://127.0.0.1:5000/checkout")
    sleep(5)
    checkout_page = CheckoutPage(browser)

    btn_link = browser.find_element(By.CSS_SELECTOR, ".btn-link")
    sleep(5)

    btn_link.click()
    sleep(5)

    assert "Cart" in browser.title
    # 장바구니로 돌아가기!
    #browser.get("http://127.0.0.1:5000/cart")

def test_go_to_cancel_page(browser):
    clean_session(browser)
    browser.get("http://127.0.0.1:5000")
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

    alert_window = browser.find_element(By.CSS_SELECTOR, ".alert-success")

    # 결제페이지
    browser.get("http://127.0.0.1:5000/checkout")
    sleep(5)
    checkout_page = CheckoutPage(browser)

    cancel = browser.find_element(By.CSS_SELECTOR, ".btn-outline-secondary")
    sleep(5)

    cancel.click()
    sleep(5)

    # 결제취소하기
    alert_window = browser.find_element(By.CSS_SELECTOR, ".alert.alert-info.mb-2")
    assert "결제가 취소되었습니다." == alert_window.text.strip()
