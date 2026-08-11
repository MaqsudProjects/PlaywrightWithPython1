import time

from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        page=browser.new_page()
        page.goto("https://facebook.com")
        time.sleep(2)
        #email_textbox=page.locator("[id='_R_1h6kqsqppb6amH1_']")
        # page.get_by_role("input",name="email")
        # time.sleep(2)
        # email_textbox.fill("Maqsud")
        # Fill out the email field using its role and accessible name
        email_text=page.get_by_role("textbox", name="email")
        email_text.fill("memon@example.com")
        result_email=email_text.input_value()
        print(f"actual email::{result_email}")
        # Fill out the password field
        pass_text=page.get_by_role("textbox", name="Password")
        pass_text.fill("m1e2123")
        #get_by_text
        verify_caption=page.get_by_text("Log in to Facebook",exact=True)
        print(verify_caption.inner_text())
        page.screenshot(path="fb.png")
        time.sleep(2)
        browser.close()

if __name__=="__main__":
    run()