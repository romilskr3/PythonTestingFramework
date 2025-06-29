import json
import pytest
from playwright.sync_api import sync_playwright

# Load config.json once at startup
with open("config.json") as f:
    config = json.load(f)

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser_type = config.get("browser", "chromium")
        headless = config.get("headless", True)
        slow_mo = config.get("slow_mo", 0)

        browser = getattr(p, browser_type).launch(headless=headless, slow_mo=slow_mo)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

@pytest.fixture(scope="session")
def base_url():
    return config.get("base_url")
