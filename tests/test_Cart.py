from config.base import BASE_ROOT, INVENTORY_ENDPOINT, DETAILED_ITEM_ENDPOINT, \
    CARD_BADGE_ENDPOINT
from config.products import SAUCE_LABS_BACKPACK, SAUCE_LABS_BIKE_LIGHT, \
    SAUCE_LABS_BOLT_TSHIRT
from config.users import ERROR_USER, PASSWORD
from pages.card_page import CardPage
from pages.detail_page import DetailPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage



def test_tc_cart_001(auth_page):
    auth_page.goto(BASE_ROOT + INVENTORY_ENDPOINT)

    inventory_page = InventoryPage(auth_page)
    inventory_page.validate_url(BASE_ROOT + INVENTORY_ENDPOINT)
    inventory_page.add_product_to_cart([SAUCE_LABS_BACKPACK])
    inventory_page.validate_value_of_cart_badge("1")

def test_tc_cart_002(auth_page):
    auth_page.goto(BASE_ROOT + INVENTORY_ENDPOINT)

    inventory_page = InventoryPage(auth_page)
    inventory_page.validate_url(BASE_ROOT + INVENTORY_ENDPOINT)
    inventory_page.add_product_to_cart([SAUCE_LABS_BACKPACK, SAUCE_LABS_BIKE_LIGHT, SAUCE_LABS_BOLT_TSHIRT])
    inventory_page.validate_value_of_cart_badge("3")

def test_tc_cart_003(auth_page):
    auth_page.goto(BASE_ROOT + INVENTORY_ENDPOINT)

    inventory_page = InventoryPage(auth_page)
    inventory_page.validate_url(BASE_ROOT + INVENTORY_ENDPOINT)
    inventory_page.add_product_to_cart([SAUCE_LABS_BACKPACK], 3)
    inventory_page.validate_value_of_cart_badge("1")

def test_tc_cart_004(auth_page):
    auth_page.goto(BASE_ROOT + INVENTORY_ENDPOINT)

    inventory_page = InventoryPage(auth_page)
    inventory_page.validate_url(BASE_ROOT + INVENTORY_ENDPOINT)
    inventory_page.add_product_to_cart([SAUCE_LABS_BACKPACK])
    inventory_page.validate_value_of_cart_badge("1")
    inventory_page.validate_presence_of_remove_btn_on_product(SAUCE_LABS_BACKPACK)
    inventory_page.remove_product_from_cart_badge(SAUCE_LABS_BACKPACK)
    inventory_page.validate_cart_badge_is_empty()

def test_tc_cart_005(auth_page):
    pass
    # нету возможности увеличить количества товара (+\-)

def test_tc_cart_006(auth_page):
    auth_page.goto(BASE_ROOT + DETAILED_ITEM_ENDPOINT)

    detailed_page = DetailPage(auth_page)
    detailed_page.click_to_card_link_btn()

    card_page = CardPage(auth_page)
    card_page.validate_url(BASE_ROOT + CARD_BADGE_ENDPOINT)

def test_tc_cart_007(auth_page):
    auth_page.goto(BASE_ROOT + CARD_BADGE_ENDPOINT)

    card_page = CardPage(auth_page)
    card_page.click_on_continue_shopping()

    inventory_page = InventoryPage(auth_page)
    inventory_page.validate_url(BASE_ROOT + INVENTORY_ENDPOINT)

def test_tc_cart_008(auth_page):
    auth_page.goto(BASE_ROOT + INVENTORY_ENDPOINT)

    inventory_page = InventoryPage(auth_page)
    inventory_page.click_to_card_link_btn()

    card_page = CardPage(auth_page)
    card_page.validate_cart_badge_is_empty()

def test_tc_cart_009(auth_page):
    auth_page.goto(BASE_ROOT + INVENTORY_ENDPOINT)

    inventory_page = InventoryPage(auth_page)
    inventory_page.add_product_to_cart([SAUCE_LABS_BACKPACK])
    inventory_page.validate_value_of_cart_badge("1")
    inventory_page.reload_page()
    inventory_page.validate_value_of_cart_badge("1")

def test_tc_cart_010(auth_page):
    auth_page.goto(BASE_ROOT + INVENTORY_ENDPOINT)

    inventory_page = InventoryPage(auth_page)
    inventory_page.add_product_to_cart([SAUCE_LABS_BACKPACK])
    inventory_page.validate_value_of_cart_badge("1")
    inventory_page.click_on_menu_btn()
    inventory_page.click_on_logout_btn()

    login_page = LoginPage(auth_page)
    login_page.login_process(ERROR_USER, PASSWORD)
    inventory_page.validate_cart_badge_is_empty()  ## тут уже баг страницы. При авторизации с другого юзера, в корзине сохранена кеш предыдущего юзера
