from playwright.sync_api import Page

class LoginPage:

    def __init__(self, page: Page):
        self.page = page

        self.username = page.locator("#_R_1h6kqsqppb6amH1_")
        self.password = page.locator("#_R_1hmkqsqppb6amH1_")
        # self.login_btn = page.locator("#login")
        # self.error_msg = page.locator(".error")

    def navigate(self):
        self.page.goto("https://facebook.com")

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        # self.login_btn.click()

    # def get_error_message(self):
    #     return self.error_msg.text_content()