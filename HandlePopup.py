from playwright.sync_api import Playwright,expect

from typing import re
def run():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        page=browser.new_page()
        page.goto("https://the-internet.herokuapp.com/javascript_alerts")
        

