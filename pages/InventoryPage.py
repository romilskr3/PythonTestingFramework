class InventoryPage:
    def __init__(self, page):
        self.page = page

    def is_logged_in(self):
        assert self.page.locator(".title").inner_text() == "Products"

    def add_item_to_cart(self, item_id):
        self.page.click(f"//*[@id='add-to-cart-{item_id}']")

    def verify_items_count_in_cart(self, expected_count):
        cart_badge = self.page.locator("//*[@class='shopping_cart_badge']")
        assert cart_badge.is_visible(), "Cart badge is not visible"
        assert cart_badge.text_content() == str(expected_count), f"Expected {expected_count} items in cart, found {cart_badge.text_content()}"

    def go_to_cart(self):
        self.page.click("#shopping_cart_container")