from pages.login_page import LoginPage
from pages.InventoryPage import InventoryPage
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage

def test_checkout_process(page, base_url):
    page.goto(base_url)

    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")
    inventory_page = InventoryPage(page)
    inventory_page.is_logged_in()
    inventory_page.add_item_to_cart("sauce-labs-bike-light")
    inventory_page.add_item_to_cart("sauce-labs-backpack")
    inventory_page.verify_items_count_in_cart(2)
    inventory_page.go_to_cart()

    cart_page = CartPage(page)
    cart_page.is_cart_page()
    cart_page.verify_item_in_cart("Sauce Labs Bike Light")
    cart_page.verify_item_in_cart("Sauce Labs Backpack")
    cart_page.proceed_to_checkout()

    checkout_page = CheckoutPage(page)
    checkout_page.fill_checkout_info("TestFN", "TestLN", "12345")
    checkout_page.proceed_to_checkout_overview()
    checkout_page.verify_checkout_overview() #can be more generic
    checkout_page.finish_checkout()