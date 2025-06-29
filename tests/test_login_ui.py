from pages.login_page import LoginPage

def test_login_success(page, base_url):
    # Navigate using base_url from config.json
    page.goto(base_url)

    LoginPage(page).login("standard_user", "secret_sauce")

    # Verify successful login by checking for the inventory page element
    assert page.url.endswith("/inventory.html")
    assert page.locator("//*[@class='inventory_container']").is_visible()

    #Verify that the user is logged in by checking the title
    assert LoginPage(page).is_logged_in()

def test_login_failure(page, base_url):
    # Navigate using base_url from config.json
    page.goto(base_url)

    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauc")

    # Verify error message is displayed
    assert page.locator("//*[@id='login_button_container']//h3").is_visible()
    assert page.locator("//*[@id='login_button_container']//h3").text_content() == "Epic sadface: Username and password do not match any user in this service"