import pytest
from playwright.sync_api import sync_playwright

from config.base import BASE_URL, BASE_ROOT, INVENTORY_ENDPOINT
from config.users import STANDARD_USER, PASSWORD
from pages.login_page import LoginPage


@pytest.fixture(scope="session", autouse=True)
def create_auth():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        login_page = LoginPage(page)
        login_page.open_page(BASE_URL)
        login_page.login_procedure(STANDARD_USER, PASSWORD)
        login_page.validate_url(BASE_ROOT + INVENTORY_ENDPOINT)

        context.storage_state(path="auth.json")
        browser.close()


@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()


@pytest.fixture
def auth_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(storage_state="auth.json")
        page = context.new_page()
        yield page
        context.close()