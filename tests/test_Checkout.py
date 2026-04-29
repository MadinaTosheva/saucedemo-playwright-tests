import pytest

from config.base import BASE_ROOT, CHECKOUT_ENDPOINT, BASE_URL, \
    OVERVIEW_ENDPOINT, INVENTORY_ENDPOINT, CARD_BADGE_ENDPOINT
from config.products import SAUCE_LABS_BACKPACK, SAUCE_LABS_BIKE_LIGHT
from config.users import EMPTY_FIRSTNAME, LASTNAME, POSTAL_CODE, \
    EMPTY_FIRSTNAME_ERROR, FIRSTNAME, EMPTY_LASTNAME, EMPTY_LASTNAME_ERROR, \
    EMPTY_POSTALCODE, EMPTY_POSTAL_CODE_ERROR, POSTAL_CODE_ALPHA
from pages.card_page import CardPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
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

def test_tc_check_006(auth_page):
    auth_page.goto(BASE_ROOT + CHECKOUT_ENDPOINT)

    checkout_page = CheckoutPage(auth_page)
    checkout_page.click_cancel_btn()

    card_page = CardPage(auth_page)
    card_page.validate_url(BASE_ROOT + CARD_BADGE_ENDPOINT)

def test_tc_check_007(auth_page):
    auth_page.goto(BASE_ROOT + CHECKOUT_ENDPOINT)

    checkout_page = CheckoutPage(auth_page)
    checkout_page.click_cancel_btn()

    card_page = CardPage(auth_page)
    card_page.click_on_continue_shopping()

    inventory_page = InventoryPage(auth_page)
    inventory_page.validate_url(BASE_ROOT + INVENTORY_ENDPOINT)

def test_tc_check_008(auth_page):
    auth_page.goto(BASE_ROOT + INVENTORY_ENDPOINT)

    inventory_page = InventoryPage(auth_page)
    inventory_page.add_product_to_cart([SAUCE_LABS_BACKPACK])
    inventory_page.click_to_card_badge_btn()

    card_page = CardPage(auth_page)
    card_page.click_on_checkout_btn()

    checkout_page = CheckoutPage(auth_page)
    checkout_page.checkout_process(FIRSTNAME, LASTNAME, POSTAL_CODE)

    overview_page = OverviewPage(auth_page)
    overview_page.validate_url(BASE_ROOT + OVERVIEW_ENDPOINT)
    item_price = overview_page.get_item_total()
    item_tax = overview_page.get_tax()
    overview_page.validate_total_payment_amount(item_price, item_tax)

def test_tc_check_009(auth_page):
    pass
    # использовала округление суммы в методе validate_total_payment_amount()
    # где получаем округлённый тотал эмаунт

def test_tc_check_010(auth_page):
    auth_page.goto(BASE_ROOT + INVENTORY_ENDPOINT)

    inventory_page = InventoryPage(auth_page)
    inventory_page.add_product_to_cart([SAUCE_LABS_BACKPACK, SAUCE_LABS_BIKE_LIGHT])
    inventory_page.click_to_card_badge_btn()

    card_page = CardPage(auth_page)
    card_page.click_on_checkout_btn()

    checkout_page = CheckoutPage(auth_page)
    checkout_page.checkout_process(FIRSTNAME, LASTNAME, POSTAL_CODE)

    overview_page = OverviewPage(auth_page)
    overview_page.validate_url(BASE_ROOT + OVERVIEW_ENDPOINT)
    item_price = overview_page.get_item_total()
    item_tax = overview_page.get_tax()
    overview_page.validate_total_payment_amount(item_price, item_tax)




