class CartPage:
    def __init__(self, page):
        self.page = page

    def is_cart_page(self):
        assert self.page.locator(".title").inner_text() == "Your Cart"

    def verify_item_in_cart(self, item_name):
        item_locator = self.page.locator(f"//div[@class='cart_item']//div[@class='inventory_item_name' and text()='{item_name}']")
        assert item_locator.is_visible(), f"Item '{item_name}' is not in the cart"

    def proceed_to_checkout(self):
        self.page.click("#checkout")