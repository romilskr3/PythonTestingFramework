class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self.checkout_button = page.locator("#checkout")
        self.first_name_input = page.locator("#first-name")
        self.last_name_input = page.locator("#last-name")
        self.postal_code_input = page.locator("#postal-code")
        self.continue_button = page.locator("#continue")
        self.finish_button = page.locator("#finish")

    def fill_checkout_info(self, first_name, last_name, postal_code):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)

    def proceed_to_checkout_overview(self):
        self.continue_button.click()
    
    def verify_checkout_overview(self):
        assert self.page.locator(".title").inner_text() == "Checkout: Overview"
        assert self.page.locator("//*[@class='inventory_item_name']").nth(0).text_content() == "Sauce Labs Bike Light"
        assert self.page.locator("//*[@class='inventory_item_name']").nth(1).text_content() == "Sauce Labs Backpack"
        total_price = self.page.locator("//*[@class='summary_total_label']").text_content()
        assert total_price == "Total: $43.18"

    def finish_checkout(self):
        self.finish_button.click()
        assert self.page.locator(".complete-header").text_content() == "Thank you for your order!"