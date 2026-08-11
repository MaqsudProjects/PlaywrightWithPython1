from playwright.sync_api import Playwright,expect,sync_playwright

def run():
        with sync_playwright() as p:
            page=p.chromium.launch(headless=False)
            browser=page.new_page()
            browser.goto("https://webapps.tekstac.com/FormRegistration/FormRegistration.html")
            browser.locator("select").wait_for(state="visible")
            #browser.locator("select").click()
            browser.locator("select").select_option("Chennai")
            data=browser.locator("select")
            for data_value in data.all_text_contents():
               print(data_value.strip().replace("Select City",""))
            input("Enter to close the browser")

if __name__=='__main__':
    run()