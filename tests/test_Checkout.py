import pytest

from config.base import BASE_ROOT, CHECKOUT_ENDPOINT, BASE_URL, \
    OVERVIEW_ENDPOINT
from config.users import EMPTY_FIRSTNAME, LASTNAME, POSTAL_CODE, \
    EMPTY_FIRSTNAME_ERROR, FIRSTNAME, EMPTY_LASTNAME, EMPTY_LASTNAME_ERROR, \
    EMPTY_POSTALCODE, EMPTY_POSTAL_CODE_ERROR, POSTAL_CODE_ALPHA
from pages.checkout_page import CheckoutPage
from pages.overview_page import OverviewPage


@pytest.mark.parametrize("firstname, lastname, postalcode, error_text",[
    (EMPTY_FIRSTNAME, LASTNAME, POSTAL_CODE, EMPTY_FIRSTNAME_ERROR),
    (FIRSTNAME, EMPTY_LASTNAME, POSTAL_CODE, EMPTY_LASTNAME_ERROR),
    (FIRSTNAME, LASTNAME, EMPTY_POSTALCODE, EMPTY_POSTAL_CODE_ERROR)])

def test_tc_check_002_003_004(auth_page, firstname, lastname, postalcode, error_text):
    auth_page.goto(BASE_ROOT + CHECKOUT_ENDPOINT)

    checkout_page = CheckoutPage(auth_page)
    checkout_page.checkout_process(firstname, lastname, postalcode)
    checkout_page.error_check(error_text)

def test_tc_check_005(auth_page):
    auth_page.goto(BASE_ROOT + CHECKOUT_ENDPOINT)

    checkout_page = CheckoutPage(auth_page)
    checkout_page.checkout_process(FIRSTNAME, LASTNAME, POSTAL_CODE_ALPHA)

    overview_page = OverviewPage(auth_page)
    overview_page.validate_url(BASE_ROOT + OVERVIEW_ENDPOINT)

