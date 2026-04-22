import pytest

from config.base import BASE_URL, BASE_ROOT, INVENTORY_ENDPOINT
from config.users import STANDARD_USER, PASSWORD, LOCKED_OUT_USER, \
    LOCKED_OUT_USER_ERROR, WRONG_PASSWORD, NO_MATCHES_ERROR, FAKE_USER, \
    EMPTY_USER, USERNAME_EMPTY_ERROR, EMPTY_PASSWORD, PASSWORD_EMPTY_ERROR, \
    WRONG_SQL_USER, WRONG_XSS_USER
from pages.base_page import BasePage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

@pytest.mark.parametrize("username, password, error_text",[
    (LOCKED_OUT_USER, PASSWORD, LOCKED_OUT_USER_ERROR),
    (STANDARD_USER, WRONG_PASSWORD, NO_MATCHES_ERROR),
    (FAKE_USER, PASSWORD, NO_MATCHES_ERROR),
    (EMPTY_USER, PASSWORD, USERNAME_EMPTY_ERROR),
    (STANDARD_USER, EMPTY_PASSWORD, PASSWORD_EMPTY_ERROR),
    (WRONG_SQL_USER, PASSWORD, NO_MATCHES_ERROR),
    (WRONG_XSS_USER, PASSWORD, NO_MATCHES_ERROR)])

def test_negative_login(page, username, password, error_text):
    # покрывает тест кейсы от 2 до 8
    base_page = BasePage(page)
    base_page.open_page(BASE_URL)
    base_page.validate_url(BASE_URL)

    login_page = LoginPage(page)
    login_page.login_procedure(username, password)
    login_page.error_check(error_text)

def test_tc_auth_001(page):
    base_page = BasePage(page)
    base_page.open_page(BASE_URL)
    base_page.validate_url(BASE_URL)

    login_page = LoginPage(page)
    login_page.login_procedure(STANDARD_USER, PASSWORD)

    inventory_page = InventoryPage(page)
    inventory_page.validate_url(BASE_ROOT + INVENTORY_ENDPOINT)

def test_tc_auth_009(page):
    base_page = BasePage(page)
    base_page.open_page(BASE_URL)
    base_page.validate_url(BASE_URL)
    # пять неуспешных попыток авторизации

    for i in range(5):
        login_page = LoginPage(page)
        login_page.login_procedure(LOCKED_OUT_USER, PASSWORD)

    # шестая попытка успешная (без блокировки страницы)
    login_page = LoginPage(page)
    login_page.login_procedure(STANDARD_USER, PASSWORD)

    inventory_page = InventoryPage(page)
    inventory_page.validate_url(BASE_ROOT + INVENTORY_ENDPOINT)

def test_tc_auth_010(page):
    base_page = BasePage(page)
    base_page.open_page(BASE_URL)
    base_page.validate_url(BASE_URL)

    login_page = LoginPage(page)
    login_page.login_procedure(STANDARD_USER, PASSWORD)

    inventory_page = InventoryPage(page)
    inventory_page.validate_url(BASE_ROOT + INVENTORY_ENDPOINT)
    inventory_page.reload_page()
    inventory_page.validate_url(BASE_ROOT + INVENTORY_ENDPOINT)
