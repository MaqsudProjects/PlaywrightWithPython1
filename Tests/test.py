from Pages.login_page import LoginPage
# from pages.dashboard_page import DashboardPage
import conftest

def test_valid_login(page):

    login = LoginPage(page)
    # dashboard = DashboardPage(page)

    login.navigate()
    login.login("admin", "password123")
    page.wait_for_timeout(2000)
    #input("Press any key to close the browser")
    # assert dashboard.get_welcome_message() == "Welcome"