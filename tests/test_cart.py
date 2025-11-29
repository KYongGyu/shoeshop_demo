import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.smoke
def test_add_remove_cart_from_inventory(login_standard):
    # 로그인된 상태로, 장바구니에서 상품을 추가하고 제거하여 장바구니 카운트를 검증
    inv = login_standard
    names = inv.item_names()[:2]
    inv.add_item(names[0])
    inv.add_item(names[1])
    inv.wait_cart_count(2) # 상품을 추가한 후 장바구니 아이템 수가 2개인지 확인
    inv.remove_item(names[1])
    inv.wait_cart_count(1) # 상품을 제거한 후 장바구니 아이템 수가 1개인지 확인

@pytest.mark.regression
def test_remove_item_in_cart_page(login_standard):
    # 장바구니에서 상품을 제거하고, 상품이 제거되었는지 검증
    inv = login_standard
    name = inv.item_names()[0]
    inv.add_item(name)
    inv.wait_cart_count(1)
    inv.go_cart()
    cart = CartPage(inv.driver)
    assert len(cart.items()) == 1 # 장바구니에 1개의 아이템이 있는지 확인
    cart.remove(name)
    item_names_after_removal = cart.item_name()
    assert name not in item_names_after_removal # 상품이 장바구니에서 제거되었는지 확인
    assert len(cart.items()) == 0 # 장바구니가 비어 있는지 확인

@pytest.mark.smoke
def test_total_math(login_standard):
    # 장바구니의 총 금액이 올바르게 계산되었는지 검증
    inv = login_standard
    total = 0
    for n in inv.item_names()[:2]:
        inv.add_item(n)
        total += inv.item_price(n) # 각 아이템의 가격을 총합에 더함
    inv.wait_cart_count(2)
    assert round(inv.item_total(), 2) == round(total, 2) #계산된 총액과 실제 금액이 일치하는지 확인

@pytest.mark.regression
def test_continue_shopping_returns_inventory(login_standard):
    # 쇼핑 계속하기 버튼을 눌러 인벤토리 페이지로 돌아가는지 확인
    inv = login_standard
    inv.add_item(inv.item_names()[0])
    inv.wait_cart_count(1)
    inv.go_cart()
    cart = CartPage(inv.driver)
    cart.continue_shopping() # 쇼핑 계속하기 버튼 클릭
    assert "inventory" in inv.driver.current_url # 인벤토리 페이지로 돌아갔는지 확인

def _go_checkout(inv):
    # 결제 페이지로 이동하여, 결제 버튼 클릭 후 URL 확인
    inv.add_item(inv.item_names()[0])
    inv.wait_cart_count(1)
    inv.go_cart()
    cart = CartPage(inv.driver)
    cart.checkout() # 결제 버튼 클릭
    assert "checkout" in inv.driver.current_url # 결제 페이지로 이동했는지 확인
    return CheckoutPage(inv.driver) #CheckoutPage로 이동 후 반환
