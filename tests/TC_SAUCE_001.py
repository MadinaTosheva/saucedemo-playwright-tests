from config.base import BASE_ROOT, INVENTORY_ENDPOINT, BASE_URL, \
    CARD_BADGE_ENDPOINT
from config.users import STANDARD_USER, PASSWORD
from pages.base_page import BasePage
from pages.card_page import CardPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_tc_sauce_001(page):
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
    inventory_page.validate_presence_of_product()
    price_text = inventory_page.get_product_price()
    inventory_page.validate_product_price(price_text)

    inventory_page.click_add_to_cart_btn()
    inventory_page.validate_presence_of_remove_btn()
    inventory_page.validate_value_of_cart_badge()
    inventory_page.click_to_card_badge_btn()

    card_page = CardPage(page)
    card_page.validate_url(BASE_ROOT + CARD_BADGE_ENDPOINT)
    card_page.validate_item_quantity()



