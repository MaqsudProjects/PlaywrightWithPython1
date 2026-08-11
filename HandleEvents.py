from playwright.sync_api import Playwright,expect,sync_playwright
from playwright.sync_api import Dialog as dialog

def handle_dialog(dialog):
     print(dialog.message)
     dialog.accept()

def handle_dialog1(dialog):
     print(dialog.message)
     dialog.dismiss()

with sync_playwright() as p:
     page=p.chromium.launch(headless=False)
     browser=page.new_page()
     browser.goto("https://the-internet.herokuapp.com/javascript_alerts")
     browser.once("dialog",handle_dialog)
     alert_popup=browser.locator("//button[text()='Click for JS Alert']")
     alert_popup.wait_for(state="visible")
     alert_popup.click()
     browser.wait_for_timeout(2000)
     #browser.wait_for_load_state("load")
     browser.once("dialog",handle_dialog1)
     confirm_popup=browser.locator("//button[text()='Click for JS Confirm']")
     confirm_popup.wait_for(state="visible")
     confirm_popup.click()
     browser.wait_for_timeout(2000)
     input("Press Enter to close the browser")