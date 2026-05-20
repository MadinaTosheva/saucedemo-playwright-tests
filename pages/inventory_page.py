import allure
from playwright.sync_api import expect

from config.products import SAUCE_LABS_BACKPACK, ITEMS_LIST
from pages.base_page import BasePage


class InventoryPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.backpack = self.page.get_by_text(SAUCE_LABS_BACKPACK)
        self.price = self.page.locator("(//div[@class='pricebar'])[1]"
                                       "/div[@class='inventory_item_price']")
        self.add_backpack_to_cart = self.page.locator(
            "#add-to-cart-sauce-labs-backpack")
        self.remove = self.page.locator("#remove-sauce-labs-backpack")
        self.cart_badge = self.page.locator(".shopping_cart_badge")
        self.cart_link = self.page.locator(".shopping_cart_link")
        self.inventory_items = self.page.locator('.inventory_item')
        self.inventory_list = self.page.locator(".inventory_list")
        self.inventory_item_name = self.page.locator(".inventory_item_name ")
        self.inventory_item_price = self.page.locator(".inventory_item_price")
        self.inventory_images = self.page.locator(".inventory_item_img a img")
        self.sort_container = self.page.locator(".product_sort_container")
        self.menu_btn = self.page.locator("#react-burger-menu-btn")
        self.logout_btn = self.page.locator("#logout_sidebar_link")

    @allure.step("Validate backpack is visible on the page")
    def validate_presence_of_product(self):
        expect(self.backpack).to_be_visible()

    @allure.step("Get product price")
    def get_product_price(self):
        return self.price.inner_text()

    @allure.step("Validate product price starts with '$'")
    def validate_product_price(self, price_text: str):
        assert price_text.startswith("$")

    @allure.step("Locate product item by name: '{product_name}'")
    def loc_product_item_by_text(self, product_name: str):
        return self.page.locator(".inventory_item", has_text=product_name)

    @allure.step("Add products to cart: '{product_names}'")
    def add_product_to_cart(self, product_names: list, click_count=1):
        for name in product_names:
            product = self.loc_product_item_by_text(name)
            product.get_by_text("Add to cart").click(click_count=click_count)

    @allure.step("Validate Remove button is present on product: '{product_name}'")
    def validate_presence_of_remove_btn_on_product(self, product_name: str):
        product = self.loc_product_item_by_text(product_name)
        expect(product).to_contain_text("Remove")

    @allure.step("Remove product from cart: '{product_name}'")
    def remove_product_from_cart_badge(self, product_name):
        product = self.page.locator(".inventory_item", has_text=product_name)
        product.get_by_text("Remove").click()

    @allure.step("Validate cart badge value is '{num}'")
    def validate_value_of_cart_badge(self, num):
        expect(self.cart_badge).to_have_text(num)

    @allure.step("Validate cart badge is empty")
    def validate_cart_badge_is_empty(self):
        expect(self.cart_badge).to_have_count(0)

    @allure.step("Click cart link button")
    def click_to_card_link_btn(self):
        self.cart_link.click()

    @allure.step("Click cart badge button")
    def click_to_card_badge_btn(self):
        self.cart_badge.click()

    @allure.step("Reload page")
    def reload_page(self):
        self.page.reload()

    @allure.step("Validate inventory item count is '{num}'")
    def validate_item_count(self, num):
        expect(self.inventory_items).to_have_count(num)

    @allure.step("Validate items are present: '{items}'")
    def validate_items_name(self, items):
        for i in items:
            expect(self.inventory_list).to_contain_text(i)

    @allure.step("Get all items prices")
    def get_items_prices(self):
        prices = {}
        for i in range(self.inventory_items.count()):
            item = self.inventory_items.nth(i)
            name = item.locator(self.inventory_item_name).inner_text()
            price = item.locator(self.inventory_item_price).inner_text()
            price = float(price.replace("$", ""))
            prices[name] = price
        return prices

    @allure.step("Validate all product images are loaded")
    def check_images(self):
        for i in range(self.inventory_images.count()):
            img = self.inventory_images.nth(i)
            assert img.evaluate(
                "el => el.naturalWidth > 0"), f"Broken image at index {i}"

    @allure.step("Sort products by price low to high")
    def sort_to_price_increasing(self):
        self.sort_container.select_option("lohi")

    @allure.step("Validate products are sorted by price low to high")
    def validate_price_increasing(self):
        prices = self.get_items_prices()
        actual_values = list(prices.values())
        assert actual_values == sorted(actual_values)

    @allure.step("Sort products by price high to low")
    def sort_to_price_decreasing(self):
        self.sort_container.select_option("hilo")

    @allure.step("Validate products are sorted by price high to low")
    def validate_price_decreasing(self):
        prices = self.get_items_prices()
        actual_values = list(prices.values())
        assert actual_values == sorted(actual_values, reverse=True)

    @allure.step("Sort products by name A to Z")
    def sort_name_to_A_Z(self):
        self.sort_container.select_option("az")

    @allure.step("Validate products are sorted by name A to Z")
    def validate_name_A_Z(self):
        assert ITEMS_LIST == sorted(ITEMS_LIST)

    @allure.step("Click on first product image")
    def click_on_image(self):
        self.inventory_images.nth(0).click()

    @allure.step("Click on burger menu button")
    def click_on_menu_btn(self):
        self.menu_btn.click()

    @allure.step("Click on logout button")
    def click_on_logout_btn(self):
        self.logout_btn.click()
