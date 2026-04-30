import allure

from config.base import BASE_ROOT, INVENTORY_ENDPOINT, DETAILED_ITEM_ENDPOINT
from config.products import *
from pages.detail_page import DetailPage
from pages.inventory_page import InventoryPage


@allure.epic("Saucedemo")
@allure.feature("Inventory")
class TestInventory:

    @allure.story("Inventory page content")
    @allure.title("Inventory page displays 6 products")
    @allure.severity(allure.severity_level.NORMAL)
    def test_tc_inv_001(self, auth_page):
        auth_page.goto(BASE_ROOT + INVENTORY_ENDPOINT)

        inventory_page = InventoryPage(auth_page)
        inventory_page.validate_url(BASE_ROOT + INVENTORY_ENDPOINT)
        inventory_page.validate_item_count(6)

    @allure.story("Inventory page content")
    @allure.title("Inventory page displays correct product names")
    @allure.severity(allure.severity_level.NORMAL)
    def test_tc_inv_002(self, auth_page):
        auth_page.goto(BASE_ROOT + INVENTORY_ENDPOINT)

        inventory_page = InventoryPage(auth_page)
        inventory_page.validate_url(BASE_ROOT + INVENTORY_ENDPOINT)
        inventory_page.validate_items_name(ITEMS_LIST)

    @allure.story("Inventory page content")
    @allure.title("Inventory page displays correct product prices")
    @allure.severity(allure.severity_level.NORMAL)
    def test_tc_inv_003(self, auth_page):
        auth_page.goto(BASE_ROOT + INVENTORY_ENDPOINT)

        inventory_page = InventoryPage(auth_page)
        inventory_page.validate_url(BASE_ROOT + INVENTORY_ENDPOINT)
        actual_prices = inventory_page.get_items_prices()
        assert actual_prices == ITEMS_PRICES

    @allure.story("Inventory page content")
    @allure.title("All product images are loaded without broken links")
    @allure.severity(allure.severity_level.NORMAL)
    def test_tc_inv_004(self, auth_page):
        auth_page.goto(BASE_ROOT + INVENTORY_ENDPOINT)

        inventory_page = InventoryPage(auth_page)
        inventory_page.validate_url(BASE_ROOT + INVENTORY_ENDPOINT)
        inventory_page.check_images()

    @allure.story("Product sorting")
    @allure.title("Sort products by price low to high")
    @allure.severity(allure.severity_level.NORMAL)
    def test_tc_inv_005(self, auth_page):
        auth_page.goto(BASE_ROOT + INVENTORY_ENDPOINT)

        inventory_page = InventoryPage(auth_page)
        inventory_page.validate_url(BASE_ROOT + INVENTORY_ENDPOINT)
        inventory_page.sort_to_price_increasing()
        inventory_page.validate_price_increasing()

    @allure.story("Product sorting")
    @allure.title("Sort products by price high to low")
    @allure.severity(allure.severity_level.NORMAL)
    def test_tc_inv_006(self, auth_page):
        auth_page.goto(BASE_ROOT + INVENTORY_ENDPOINT)

        inventory_page = InventoryPage(auth_page)
        inventory_page.validate_url(BASE_ROOT + INVENTORY_ENDPOINT)
        inventory_page.sort_to_price_decreasing()
        inventory_page.validate_price_decreasing()

    @allure.story("Product sorting")
    @allure.title("Sort products by name A to Z")
    @allure.severity(allure.severity_level.NORMAL)
    def test_tc_inv_007(self, auth_page):
        auth_page.goto(BASE_ROOT + INVENTORY_ENDPOINT)

        inventory_page = InventoryPage(auth_page)
        inventory_page.validate_url(BASE_ROOT + INVENTORY_ENDPOINT)
        inventory_page.sort_name_to_A_Z()
        inventory_page.validate_name_A_Z()

    @allure.story("Product sorting")
    @allure.title("Product remains in cart after sorting")
    @allure.severity(allure.severity_level.NORMAL)
    def test_tc_inv_008(self, auth_page):
        auth_page.goto(BASE_ROOT + INVENTORY_ENDPOINT)

        inventory_page = InventoryPage(auth_page)
        inventory_page.validate_url(BASE_ROOT + INVENTORY_ENDPOINT)
        inventory_page.add_product_to_cart([SAUCE_LABS_BACKPACK])
        inventory_page.sort_to_price_increasing()
        inventory_page.validate_presence_of_product()

    @allure.story("Product navigation")
    @allure.title("Click on product image navigates to detail page")
    @allure.severity(allure.severity_level.NORMAL)
    def test_tc_inv_009(self, auth_page):
        auth_page.goto(BASE_ROOT + INVENTORY_ENDPOINT)

        inventory_page = InventoryPage(auth_page)
        inventory_page.validate_url(BASE_ROOT + INVENTORY_ENDPOINT)
        inventory_page.click_on_image()

        detail_page = DetailPage(auth_page)
        detail_page.validate_url(BASE_ROOT + DETAILED_ITEM_ENDPOINT)

    @allure.story("Add product to cart")
    @allure.title("Add product to cart from inventory page")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_tc_inv_010(self, auth_page):
        auth_page.goto(BASE_ROOT + INVENTORY_ENDPOINT)

        inventory_page = InventoryPage(auth_page)
        inventory_page.validate_url(BASE_ROOT + INVENTORY_ENDPOINT)
        inventory_page.add_product_to_cart([SAUCE_LABS_BACKPACK])
        inventory_page.validate_presence_of_remove_btn_on_product(SAUCE_LABS_BACKPACK)
        inventory_page.validate_value_of_cart_badge("1")