class LoginPage:
    def __init__(self, page):
        self.page = page

    def login(self, username, password):
        self.page.fill("#user-name", username)
        self.page.fill("#password", password)
        self.page.click("#login-button")
    
    def is_logged_in(self):
        return self.page.locator(".title").inner_text() == "Products"