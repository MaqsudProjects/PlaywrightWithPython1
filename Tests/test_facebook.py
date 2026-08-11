import pytest
from playwright.sync_api import sync_playwright


def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()

        context.tracing.start(
            screenshots=True,
            snapshots=True,
            sources=True
        )

        page = context.new_page()

        try:
            page.goto("https://facebook.com")
            breakpoint()
            page.get_by_role("button", name="Login").click()
            # test steps...
        finally:
            context.tracing.stop(path="trace.zip")
            browser.close()