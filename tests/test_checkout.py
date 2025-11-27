import pytest
from saucedemo.pages.cart_page import cart_page
from saucedemo.pages.checkout_page import checkoutPage
from saucedemo.untils.data_factory import default_checkout_into

def_go_checkout(inv):
    inv.add_item(inv.item_names()[0])
    inv.wait_cart_count(1)
    inv.go_cart()
    CartPage(inv.driver).checkout()
    return CheckoutPage(inv.driver)

@pytest.mark.negative
def test_checkout_required_first_name(login_standard):
    chk=_go_checkout()