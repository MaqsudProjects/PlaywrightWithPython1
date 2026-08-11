from playwright.sync_api import Playwright,expect,sync_playwright
from playwright.sync_api import Dialog as dialog
from playwright.sync_api import Page as page

with sync_playwright() as p:
    page = p.chromium.launch(headless=False)
    browser = page.new_page()
    browser.goto("https://google.com")
    with browser.expect_download() as download_info:
        search_download = browser.get_by_role("combobox")
        search_download.fill("html:pdf")




    # search_download=browser.get_by_role("combobox")
    # search_download.fill("html:pdf")
    # browser.keyboard.press("Enter")
    input("Press Enter to close the browser")