import pytest
from shoeshop_demo.pages.cart_page import CartPage

@pytest.mark.smoke
def test_add_remove_cart_from_inventory(login_standard):
    inv = login_standard
    names = inv.item_names()[:2]
    inv.add_item(names[0])
    inv.add_item(names[1])
    inv.wait_cart_count(2)
    inv.remove_item(names[1])
    inv.wait_cart_count(1)

@pytest.mark.regression
def test_remove_item_in_cart_page(login_standard):
    inv = login_standard
    name = inv.item_names()[0]
    inv.add_item(name)
    inv.wait_cart_count(1)
    inv.go_cart()
    cart = CartPage(inv.driver)
    assert len(cart.items()) == 1
    cart.remove(name)
    item_names_after_removal = cart.item_name()
    assert name not in item_names_after_removal
    assert len(cart.items()) == 0

@pytest.mark.smoke
def test_total_math(login_standard):
    inv = login_standard
    total = 0
    for n in inv.item_names()[:2]:
        inv.add_item(n)
        total += inv.item_price(n)
    inv.wait_cart_count(2)
    assert round(inv.item_total(), 2) == round(total, 2)

@pytest.mark.regression
def test_continue_shopping_returns_inventory(login_standard):
    inv = login_standard
    inv.add_item(inv.item_names()[0])
    inv.wait_cart_count(1)
    inv.go_cart()
    cart = CartPage(inv.driver)
    cart.continue_shopping()
    assert "inventory" in inv.driver.current_url

def _go_checkout(inv):
    inv.add_item(inv.item_names()[0])
    inv.wait_cart_count(1)
    inv.go_cart()
    cart = CartPage(inv.driver)
    cart.checkout()
    assert "checkout" in inv.driver.current_url
    return CheckoutPage(inv.driver)