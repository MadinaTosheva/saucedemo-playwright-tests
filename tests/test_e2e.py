import allure

from config.base import BASE_ROOT, INVENTORY_ENDPOINT, BASE_URL, \
    CARD_BADGE_ENDPOINT, CHECKOUT_ENDPOINT, OVERVIEW_ENDPOINT, \
    COMPLETE_ENDPOINT
from config.products import SAUCE_LABS_BACKPACK, SHIPPING_INFO_TEXT, \
     TITLE_TEXT, HEADER_TEXT, COMPLETE_TEXT
from config.users import STANDARD_USER, PASSWORD, FIRSTNAME, LASTNAME, \
    POSTAL_CODE
from pages.base_page import BasePage
from pages.card_page import CardPage
from pages.checkout_page import CheckoutPage
from pages.complete_page import CompletePage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from pages.overview_page import OverviewPage


@allure.epic("Saucedemo")
@allure.feature("E2E")
class TestE2E:

    @allure.story("Full E2E purchase flow")
    @allure.title("Complete purchase flow from login to order confirmation")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_tc_check_001(self, page):
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

        inventory_page.add_product_to_cart([SAUCE_LABS_BACKPACK])
        inventory_page.validate_presence_of_remove_btn_on_product(SAUCE_LABS_BACKPACK)
        inventory_page.validate_value_of_cart_badge("1")
        inventory_page.click_to_card_badge_btn()

        card_page = CardPage(page)
        card_page.validate_url(BASE_ROOT + CARD_BADGE_ENDPOINT)
        card_page.validate_item_quantity()
        card_page.validate_product_name(SAUCE_LABS_BACKPACK)
        card_page.validate_product_price(price_text)
        card_page.click_on_checkout_btn()

        checkout_page = CheckoutPage(page)
        checkout_page.validate_url(BASE_ROOT + CHECKOUT_ENDPOINT)
        checkout_page.enter_firstname(FIRSTNAME)
        checkout_page.validate_firstname(FIRSTNAME)
        checkout_page.enter_lastname(LASTNAME)
        checkout_page.validate_lastname(LASTNAME)
        checkout_page.enter_postalcode(POSTAL_CODE)
        checkout_page.validate_postalcode(POSTAL_CODE)
        checkout_page.click_continue_btn()

        overview_page = OverviewPage(page)
        overview_page.validate_url(BASE_ROOT + OVERVIEW_ENDPOINT)
        overview_page.validate_item_quantity("1")
        overview_page.validate_item_name(SAUCE_LABS_BACKPACK)
        overview_page.validate_item_price(price_text)
        overview_page.validate_shipping_info_text(SHIPPING_INFO_TEXT)
        overview_page.validate_total_price(price_text)
        total_price = overview_page.get_item_total()
        overview_page.validate_tax_amount("2.40")
        tax = overview_page.get_tax()
        overview_page.validate_total_payment_amount(total_price, tax)
        overview_page.click_on_finish_btn()

        complete_page = CompletePage(page)
        complete_page.validate_url(BASE_ROOT + COMPLETE_ENDPOINT)
        complete_page.validate_title(TITLE_TEXT)
        complete_page.validate_header_text(HEADER_TEXT)
        complete_page.validate_complete_text(COMPLETE_TEXT)
        complete_page.button_enabled()
        complete_page.click_on_back_home_btn()

        inventory_page.validate_url(BASE_ROOT + INVENTORY_ENDPOINT)
