import allure

from config.base import BASE_ROOT, INVENTORY_ENDPOINT, DETAILED_ITEM_ENDPOINT, \
    CARD_BADGE_ENDPOINT
from config.products import SAUCE_LABS_BACKPACK, SAUCE_LABS_BIKE_LIGHT, \
    SAUCE_LABS_BOLT_TSHIRT
from config.users import ERROR_USER, PASSWORD
from pages.card_page import CardPage
from pages.detail_page import DetailPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage



@allure.epic("Saucedemo")
@allure.feature("Cart")
class TestCart:

    @allure.story("Add product to cart")
    @allure.title("Add single product to cart")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_tc_cart_001(self, auth_page):
        auth_page.goto(BASE_ROOT + INVENTORY_ENDPOINT)

        inventory_page = InventoryPage(auth_page)
        inventory_page.validate_url(BASE_ROOT + INVENTORY_ENDPOINT)
        inventory_page.add_product_to_cart([SAUCE_LABS_BACKPACK])
        inventory_page.validate_value_of_cart_badge("1")

    @allure.story("Add product to cart")
    @allure.title("Add multiple products to cart")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_tc_cart_002(self, auth_page):
        auth_page.goto(BASE_ROOT + INVENTORY_ENDPOINT)

        inventory_page = InventoryPage(auth_page)
        inventory_page.validate_url(BASE_ROOT + INVENTORY_ENDPOINT)
        inventory_page.add_product_to_cart([SAUCE_LABS_BACKPACK, SAUCE_LABS_BIKE_LIGHT, SAUCE_LABS_BOLT_TSHIRT])
        inventory_page.validate_value_of_cart_badge("3")

    @allure.story("Add product to cart")
    @allure.title("Add same product multiple times - cart badge shows 1")
    @allure.severity(allure.severity_level.NORMAL)
    def test_tc_cart_003(self, auth_page):
        auth_page.goto(BASE_ROOT + INVENTORY_ENDPOINT)

        inventory_page = InventoryPage(auth_page)
        inventory_page.validate_url(BASE_ROOT + INVENTORY_ENDPOINT)
        inventory_page.add_product_to_cart([SAUCE_LABS_BACKPACK], 3)
        inventory_page.validate_value_of_cart_badge("1")

    @allure.story("Remove product from cart")
    @allure.title("Remove product from cart via Remove button")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_tc_cart_004(self, auth_page):
        auth_page.goto(BASE_ROOT + INVENTORY_ENDPOINT)

        inventory_page = InventoryPage(auth_page)
        inventory_page.validate_url(BASE_ROOT + INVENTORY_ENDPOINT)
        inventory_page.add_product_to_cart([SAUCE_LABS_BACKPACK])
        inventory_page.validate_value_of_cart_badge("1")
        inventory_page.validate_presence_of_remove_btn_on_product(SAUCE_LABS_BACKPACK)
        inventory_page.remove_product_from_cart_badge(SAUCE_LABS_BACKPACK)
        inventory_page.validate_cart_badge_is_empty()

    @allure.story("Cart navigation")
    @allure.title("Navigate to cart from product detail page")
    @allure.severity(allure.severity_level.NORMAL)
    def test_tc_cart_006(self, auth_page):
        auth_page.goto(BASE_ROOT + DETAILED_ITEM_ENDPOINT)

        detailed_page = DetailPage(auth_page)
        detailed_page.click_to_card_link_btn()

        card_page = CardPage(auth_page)
        card_page.validate_url(BASE_ROOT + CARD_BADGE_ENDPOINT)

    @allure.story("Cart navigation")
    @allure.title("Continue shopping from cart returns to inventory")
    @allure.severity(allure.severity_level.NORMAL)
    def test_tc_cart_007(self, auth_page):
        auth_page.goto(BASE_ROOT + CARD_BADGE_ENDPOINT)

        card_page = CardPage(auth_page)
        card_page.click_on_continue_shopping()

        inventory_page = InventoryPage(auth_page)
        inventory_page.validate_url(BASE_ROOT + INVENTORY_ENDPOINT)

    @allure.story("Cart state")
    @allure.title("Cart is empty when no products added")
    @allure.severity(allure.severity_level.NORMAL)
    def test_tc_cart_008(self, auth_page):
        auth_page.goto(BASE_ROOT + INVENTORY_ENDPOINT)

        inventory_page = InventoryPage(auth_page)
        inventory_page.click_to_card_link_btn()

        card_page = CardPage(auth_page)
        card_page.validate_cart_badge_is_empty()

    @allure.story("Cart state")
    @allure.title("Cart persists after page reload")
    @allure.severity(allure.severity_level.NORMAL)
    def test_tc_cart_009(self, auth_page):
        auth_page.goto(BASE_ROOT + INVENTORY_ENDPOINT)

        inventory_page = InventoryPage(auth_page)
        inventory_page.add_product_to_cart([SAUCE_LABS_BACKPACK])
        inventory_page.validate_value_of_cart_badge("1")
        inventory_page.reload_page()
        inventory_page.validate_value_of_cart_badge("1")

    @allure.story("Cart state")
    @allure.title("[BUG] Cart cache persists after logout and login with another user")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_tc_cart_010(self, auth_page):
        auth_page.goto(BASE_ROOT + INVENTORY_ENDPOINT)

        inventory_page = InventoryPage(auth_page)
        inventory_page.add_product_to_cart([SAUCE_LABS_BACKPACK])
        inventory_page.validate_value_of_cart_badge("1")
        inventory_page.click_on_menu_btn()
        inventory_page.click_on_logout_btn()

        login_page = LoginPage(auth_page)
        login_page.login_process(ERROR_USER, PASSWORD)
        inventory_page.validate_cart_badge_is_empty()