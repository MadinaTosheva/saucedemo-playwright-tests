from config.base import BASE_URL, BASE_ROOT, INVENTORY_ENDPOINT
from config.users import STANDARD_USER, PASSWORD, LOCKED_OUT_USER, \
    LOCKED_OUT_USER_ERROR, WRONG_PASSWORD, NO_MATCHES_ERROR, FAKE_USER, \
    EMPTY_USER, USERNAME_EMPTY_ERROR, EMPTY_PASSWORD, PASSWORD_EMPTY_ERROR, \
    WRONG_SQL_USER, WRONG_XSS_USER
from pages.base_page import BasePage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_tc_auth_001(page):
    base_page = BasePage(page)
    base_page.open_page(BASE_URL)
    base_page.validate_url(BASE_URL)

    login_page = LoginPage(page)
    login_page.enter_username(STANDARD_USER)
    login_page.validate_username(STANDARD_USER)
    login_page.enter_password(PASSWORD)
    login_page.validate_password(PASSWORD)
    login_page.click_login_btn()

    inventory_page = InventoryPage(page)
    inventory_page.validate_url(BASE_ROOT + INVENTORY_ENDPOINT)

def test_tc_auth_002(page):
    base_page = BasePage(page)
    base_page.open_page(BASE_URL)
    base_page.validate_url(BASE_URL)

    login_page = LoginPage(page)
    login_page.enter_username(LOCKED_OUT_USER)
    login_page.validate_username(LOCKED_OUT_USER)
    login_page.enter_password(PASSWORD)
    login_page.validate_password(PASSWORD)
    login_page.click_login_btn()
    login_page.validate_visibility_of_error()
    login_page.validate_error_text(LOCKED_OUT_USER_ERROR)

def test_tc_auth_003(page):
    base_page = BasePage(page)
    base_page.open_page(BASE_URL)
    base_page.validate_url(BASE_URL)

    login_page = LoginPage(page)
    login_page.enter_username(STANDARD_USER)
    login_page.validate_username(STANDARD_USER)
    login_page.enter_password(WRONG_PASSWORD)
    login_page.validate_password(WRONG_PASSWORD)
    login_page.click_login_btn()
    login_page.validate_visibility_of_error()
    login_page.validate_error_text(NO_MATCHES_ERROR)

def test_tc_auth_004(page):
    base_page = BasePage(page)
    base_page.open_page(BASE_URL)
    base_page.validate_url(BASE_URL)

    login_page = LoginPage(page)
    login_page.enter_username(FAKE_USER)
    login_page.validate_username(FAKE_USER)
    login_page.enter_password(PASSWORD)
    login_page.validate_password(PASSWORD)
    login_page.click_login_btn()
    login_page.validate_visibility_of_error()
    login_page.validate_error_text(NO_MATCHES_ERROR)

def test_tc_auth_005(page):
    base_page = BasePage(page)
    base_page.open_page(BASE_URL)
    base_page.validate_url(BASE_URL)

    login_page = LoginPage(page)
    login_page.enter_username(EMPTY_USER)
    login_page.validate_username(EMPTY_USER)
    login_page.enter_password(PASSWORD)
    login_page.validate_password(PASSWORD)
    login_page.click_login_btn()
    login_page.validate_visibility_of_error()
    login_page.validate_error_text(USERNAME_EMPTY_ERROR)

def test_tc_auth_006(page):
    base_page = BasePage(page)
    base_page.open_page(BASE_URL)
    base_page.validate_url(BASE_URL)

    login_page = LoginPage(page)
    login_page.enter_username(STANDARD_USER)
    login_page.validate_username(STANDARD_USER)
    login_page.enter_password(EMPTY_PASSWORD)
    login_page.validate_password(EMPTY_PASSWORD)
    login_page.click_login_btn()
    login_page.validate_visibility_of_error()
    login_page.validate_error_text(PASSWORD_EMPTY_ERROR)

def test_tc_auth_007(page):
    base_page = BasePage(page)
    base_page.open_page(BASE_URL)
    base_page.validate_url(BASE_URL)

    login_page = LoginPage(page)
    login_page.enter_username(WRONG_SQL_USER)
    login_page.validate_username(WRONG_SQL_USER)
    login_page.enter_password(PASSWORD)
    login_page.validate_password(PASSWORD)
    login_page.click_login_btn()
    login_page.validate_visibility_of_error()
    login_page.validate_error_text(NO_MATCHES_ERROR)

def test_tc_auth_008(page):
    base_page = BasePage(page)
    base_page.open_page(BASE_URL)
    base_page.validate_url(BASE_URL)

    login_page = LoginPage(page)
    login_page.enter_username(WRONG_XSS_USER)
    login_page.validate_username(WRONG_XSS_USER)
    login_page.enter_password(PASSWORD)
    login_page.validate_password(PASSWORD)
    login_page.click_login_btn()
    login_page.validate_visibility_of_error()
    login_page.validate_error_text(NO_MATCHES_ERROR)

def test_tc_auth_009(page):
    # пять неуспешных попыток авторизации
    for i in range(5):
        test_tc_auth_008(page)

    # шестая попытка успешная (без блокировки страницы)
    test_tc_auth_001(page)

def test_tc_auth_010(page):
    base_page = BasePage(page)
    base_page.open_page(BASE_URL)
    base_page.validate_url(BASE_URL)

    login_page = LoginPage(page)
    login_page.enter_username(STANDARD_USER)
    login_page.validate_username(STANDARD_USER)
    login_page.enter_password(PASSWORD)
    login_page.validate_password(PASSWORD)
    login_page.click_login_btn()

    inventory_page = InventoryPage(page)
    inventory_page.validate_url(BASE_ROOT + INVENTORY_ENDPOINT)
    inventory_page.reload_page()
    inventory_page.validate_url(BASE_ROOT + INVENTORY_ENDPOINT)


