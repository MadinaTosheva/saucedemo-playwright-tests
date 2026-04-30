import allure
import pytest

from config.base import BASE_URL, BASE_ROOT, INVENTORY_ENDPOINT
from config.users import STANDARD_USER, PASSWORD, LOCKED_OUT_USER, \
    LOCKED_OUT_USER_ERROR, WRONG_PASSWORD, NO_MATCHES_ERROR, FAKE_USER, \
    EMPTY_USER, USERNAME_EMPTY_ERROR, EMPTY_PASSWORD, PASSWORD_EMPTY_ERROR, \
    WRONG_SQL_USER, WRONG_XSS_USER
from pages.base_page import BasePage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

@allure.epic("Saucedemo")
@allure.feature("Authentication")
class TestAuth:

    @allure.story("Negative login scenarios")
    @allure.title("Login with invalid credentials: '{username}', '{password}', '{error_text}'")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("username, password, error_text", [
        (LOCKED_OUT_USER, PASSWORD, LOCKED_OUT_USER_ERROR),
        (STANDARD_USER, WRONG_PASSWORD, NO_MATCHES_ERROR),
        (FAKE_USER, PASSWORD, NO_MATCHES_ERROR),
        (EMPTY_USER, PASSWORD, USERNAME_EMPTY_ERROR),
        (STANDARD_USER, EMPTY_PASSWORD, PASSWORD_EMPTY_ERROR),
        (WRONG_SQL_USER, PASSWORD, NO_MATCHES_ERROR),
        (WRONG_XSS_USER, PASSWORD, NO_MATCHES_ERROR)])
    def test_negative_login(self, page, username, password, error_text):
        base_page = BasePage(page)
        base_page.open_page(BASE_URL)
        base_page.validate_url(BASE_URL)

        login_page = LoginPage(page)
        login_page.login_process(username, password)
        login_page.error_check(error_text)

    @allure.story("Successful login")
    @allure.title("Login with valid credentials")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_tc_auth_001(self, page):
        base_page = BasePage(page)
        base_page.open_page(BASE_URL)
        base_page.validate_url(BASE_URL)

        login_page = LoginPage(page)
        login_page.login_process(STANDARD_USER, PASSWORD)

        inventory_page = InventoryPage(page)
        inventory_page.validate_url(BASE_ROOT + INVENTORY_ENDPOINT)

    @allure.story("Successful login")
    @allure.title("Successful login after 5 failed attempts")
    @allure.severity(allure.severity_level.NORMAL)
    def test_tc_auth_009(self, page):
        base_page = BasePage(page)
        base_page.open_page(BASE_URL)
        base_page.validate_url(BASE_URL)

        for i in range(5):
            login_page = LoginPage(page)
            login_page.login_process(LOCKED_OUT_USER, PASSWORD)

        login_page = LoginPage(page)
        login_page.login_process(STANDARD_USER, PASSWORD)

        inventory_page = InventoryPage(page)
        inventory_page.validate_url(BASE_ROOT + INVENTORY_ENDPOINT)

    @allure.story("Successful login")
    @allure.title("User stays logged in after page reload")
    @allure.severity(allure.severity_level.NORMAL)
    def test_tc_auth_010(self, page):
        base_page = BasePage(page)
        base_page.open_page(BASE_URL)
        base_page.validate_url(BASE_URL)

        login_page = LoginPage(page)
        login_page.login_process(STANDARD_USER, PASSWORD)

        inventory_page = InventoryPage(page)
        inventory_page.validate_url(BASE_ROOT + INVENTORY_ENDPOINT)
        inventory_page.reload_page()
        inventory_page.validate_url(BASE_ROOT + INVENTORY_ENDPOINT)