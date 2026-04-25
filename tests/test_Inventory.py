from config.base import BASE_ROOT, INVENTORY_ENDPOINT, DETAILED_ITEM_ENDPOINT
from config.products import *
from pages.detail_page import DetailPage
from pages.inventory_page import InventoryPage


def test_tc_inv_001(auth_page):
    auth_page.goto(BASE_ROOT + INVENTORY_ENDPOINT)

    inventory_page = InventoryPage(auth_page)
    inventory_page.validate_url(BASE_ROOT + INVENTORY_ENDPOINT)
    inventory_page.validate_item_count(6)

def test_tc_inv_002(auth_page):
    auth_page.goto(BASE_ROOT + INVENTORY_ENDPOINT)

    inventory_page = InventoryPage(auth_page)
    inventory_page.validate_url(BASE_ROOT + INVENTORY_ENDPOINT)
    inventory_page.validate_items_name(ITEMS_LIST)

def test_tc_inv_003(auth_page):
    auth_page.goto(BASE_ROOT + INVENTORY_ENDPOINT)

    inventory_page = InventoryPage(auth_page)
    inventory_page.validate_url(BASE_ROOT + INVENTORY_ENDPOINT)
    actual_prices = inventory_page.get_items_prices()
    assert actual_prices == ITEMS_PRICES

def test_tc_inv_004(auth_page):
    auth_page.goto(BASE_ROOT + INVENTORY_ENDPOINT)

    inventory_page = InventoryPage(auth_page)
    inventory_page.validate_url(BASE_ROOT + INVENTORY_ENDPOINT)
    inventory_page.check_images()

def test_tc_inv_005(auth_page):
    auth_page.goto(BASE_ROOT + INVENTORY_ENDPOINT)

    inventory_page = InventoryPage(auth_page)
    inventory_page.validate_url(BASE_ROOT + INVENTORY_ENDPOINT)
    inventory_page.sort_to_price_increasing()
    inventory_page.validate_price_increasing()

def test_tc_inv_006(auth_page):
    auth_page.goto(BASE_ROOT + INVENTORY_ENDPOINT)

    inventory_page = InventoryPage(auth_page)
    inventory_page.validate_url(BASE_ROOT + INVENTORY_ENDPOINT)
    inventory_page.sort_to_price_decreasing()
    inventory_page.validate_price_decreasing()

def test_tc_inv_007(auth_page):
    auth_page.goto(BASE_ROOT + INVENTORY_ENDPOINT)

    inventory_page = InventoryPage(auth_page)
    inventory_page.validate_url(BASE_ROOT + INVENTORY_ENDPOINT)
    inventory_page.sort_name_to_A_Z()
    inventory_page.validate_name_A_Z()

def test_tc_inv_008(auth_page):
    auth_page.goto(BASE_ROOT + INVENTORY_ENDPOINT)

    inventory_page = InventoryPage(auth_page)
    inventory_page.validate_url(BASE_ROOT + INVENTORY_ENDPOINT)
    inventory_page.click_add_to_cart_btn()
    inventory_page.sort_to_price_increasing()
    inventory_page.validate_presence_of_product()

def test_tc_inv_009(auth_page):
    auth_page.goto(BASE_ROOT + INVENTORY_ENDPOINT)

    inventory_page = InventoryPage(auth_page)
    inventory_page.validate_url(BASE_ROOT + INVENTORY_ENDPOINT)
    inventory_page.click_on_image()

    detail_page = DetailPage(auth_page)
    detail_page.validate_url(BASE_ROOT + DETAILED_ITEM_ENDPOINT)

def test_tc_inv_010(auth_page):
    auth_page.goto(BASE_ROOT + INVENTORY_ENDPOINT)

    inventory_page = InventoryPage(auth_page)
    inventory_page.validate_url(BASE_ROOT + INVENTORY_ENDPOINT)
    inventory_page.click_add_to_cart_btn()
    inventory_page.validate_presence_of_remove_btn()
    inventory_page.validate_value_of_cart_badge()
