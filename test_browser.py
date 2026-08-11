import pytest
from playwright.sync_api import Playwright,expect,sync_playwright
from playwright.sync_api import Dialog as dialog

@pytest.fixture(scope="function")
def browser_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        yield page

        browser.close()

def test_login(browser_page):
    browser_page.goto("https://google.com")
    print(browser_page.title())