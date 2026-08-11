# import logging
# import conf1test
#
# logger = logging.getLogger(__name__)
#
#
# def test_login(page):
#     logger.info("Opening login page")
#
#     page.goto("https://webapps.tekstac.com/FormRegistration/FormRegistration.html")
#
#     logger.info("Entering username")
#     page.fill("#uname", "testuser")
#
#     logger.info("Entering password")
#     page.fill("#uemail", "password")
#
#     logger.info("Clicking Login")
#     page.click("#reg")
#
#     logger.info("Checking dashboard")
#     assert page.title() == "FormRegistration"
import logging
from playwright.sync_api import sync_playwright
logger = logging.getLogger(__name__)


# def test_login(page):
#     logger.info("TEST STARTED")
#
#     page.goto("https://google.com")
#
#     logger.info("PAGE OPENED")
#
#     #page.get_by_role("heading").first.wait_for()
#
#     logger.info("TEST FINISHED")



def test_browser_automation():
    logger.info("Test started")
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        page=browser.new_page()
        logger.info("Browser Launched Successfully")
        page.goto("https://facebook.com")
        page.wait_for_timeout(2000)
        current_url=page.url

        logger.info(f"Get the url,{current_url}")

    # a = 10
    # b = 20
    #
    # logger.info("a = %s", a)
    # logger.info("b = %s", b)
    #
    # result = a + b
    #
    # logger.info("Result = %s", result)
    #
    # assert result == 30

    logger.info("Test completed successfully")
