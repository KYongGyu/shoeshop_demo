import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "http://127.0.0.1:5000"


@pytest.mark.regression
def test_add_remove_from_index_page(register_and_login):
    """
    상품 목록 페이지에서 장바구니 추가 및 제거를 테스트
    """
    driver = register_and_login

    # 첫 번째 상품 찾기
    product_card = driver.find_element(By.CSS_SELECTOR, ".card")
    product_name = product_card.find_element(By.CSS_SELECTOR, ".card-title").text

    # 1. 카트에 담기 버튼 클릭
    add_button = product_card.find_element(By.CSS_SELECTOR, "button.btn-primary")
    add_button.click()

    # 장바구니 카운트 증가 확인
    cart_count = driver.find_element(By.LINK_TEXT, "Cart (1)").text
    assert "Cart (1)" in cart_count

    # 버튼이 '카트에서 제거'로 바뀌었는지 확인
    remove_button = product_card.find_element(By.CSS_SELECTOR, "button.btn-warning")
    assert remove_button.text == "카트에서 제거"
    print(f"\n[SUCCESS] '{product_name}' 장바구니 추가 확인.")

    # 2. 카트에서 제거 버튼 클릭
    remove_button.click()

    # 장바구니 카운트 감소 확인
    cart_count_empty = driver.find_element(By.LINK_TEXT, "Cart (0)").text
    assert "Cart (0)" in cart_count_empty

    # 버튼이 다시 '카트에 담기'로 바뀌었는지 확인
    add_button_again = product_card.find_element(By.CSS_SELECTOR, "button.btn-primary")
    assert add_button_again.text == "카트에 담기"
    print(f"[SUCCESS] '{product_name}' 장바구니 제거 확인.")

@pytest.mark.regression
def test_unauthenticated_cart_access(clean_session):
    """
    로그인하지 않은 상태에서 장바구니 추가 시도 시 로그인 페이지로 리다이렉션되는지 테스트
    """
    driver = clean_session

    # 첫 번째 상품의 '카트에 담기' 버튼 클릭 (로그인하지 않은 상태)
    add_button = driver.find_element(By.CSS_SELECTOR, ".card button.btn-primary")
    add_button.click()

    # 로그인 페이지로 리다이렉션되었는지 확인
    WebDriverWait(driver, 10).until(EC.url_changes(BASE_URL + "/"))
    assert driver.current_url.startswith(BASE_URL + "/login")

    # 플래시 메시지 확인
    assert "로그인이 필요합니다." in driver.find_element(By.TAG_NAME, "body").text



