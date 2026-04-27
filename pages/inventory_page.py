from playwright.sync_api import expect

from config.products import SAUCE_LABS_BACKPACK, ITEMS_LIST
from pages.base_page import BasePage


class InventoryPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.backpack = self.page.get_by_text(SAUCE_LABS_BACKPACK)
        self.price = self.page.locator("(//div[@class='pricebar'])[1]/div[@class='inventory_item_price']")
        self.add_to_cart = self.page.locator("#add-to-cart-sauce-labs-backpack")
        self.remove = self.page.locator("#remove-sauce-labs-backpack")
        self.cart_badge = self.page.locator(".shopping_cart_badge")
        self.inventory_items = self.page.locator('.inventory_item')
        self.inventory_list = self.page.locator(".inventory_list")
        self.inventory_item_name = self.page.locator(".inventory_item_name ")
        self.inventory_item_price = self.page.locator(".inventory_item_price")
        self.inventory_images = self.page.locator(".inventory_item_img a img")
        self.sort_container = self.page.locator(".product_sort_container")

    def validate_presence_of_product(self):
        expect(self.backpack).to_be_visible()

    def get_product_price(self):
        return self.price.inner_text()

    def validate_product_price(self, price_text):
        assert price_text.startswith("$")

    def click_add_to_cart_btn(self):
        self.add_to_cart.click()

    def validate_presence_of_remove_btn(self):
        expect(self.remove).to_have_text("Remove")

    def validate_value_of_cart_badge(self):
        expect(self.cart_badge).to_have_text("1")

    def click_to_card_badge_btn(self):
        self.cart_badge.click()

    def reload_page(self):
        self.page.reload()

    def validate_item_count(self, num):
        expect(self.inventory_items).to_have_count(num)

    def validate_items_name(self, items):
        for i in items:
            expect(self.inventory_list).to_contain_text(i)

    def get_items_prices(self):
        prices = {}

        for i in range(self.inventory_items.count()):
            item = self.inventory_items.nth(i)

            name = item.locator(self.inventory_item_name).inner_text()
            price = item.locator(self.inventory_item_price).inner_text()

            price = float(price.replace("$", ""))
            prices[name] = price

        return prices

    def check_images(self):
        for i in range(self.inventory_images.count()):
            img = self.inventory_images.nth(i)

            assert img.evaluate(
                "el => el.naturalWidth > 0"), f"Broken image at index {i}"

    def sort_to_price_increasing(self):
        self.sort_container.select_option("lohi")

    def validate_price_increasing(self):
        prices = self.get_items_prices()
        actual_values = list(prices.values())

        assert actual_values == sorted(actual_values)

    def sort_to_price_decreasing(self):
        self.sort_container.select_option("hilo")

    def validate_price_decreasing(self):
        prices = self.get_items_prices()
        actual_values = list(prices.values())

        assert actual_values == sorted(actual_values, reverse=True)

    def sort_name_to_A_Z(self):
        self.sort_container.select_option("az")

    def validate_name_A_Z(self):
        assert ITEMS_LIST == sorted(ITEMS_LIST)

    def click_on_image(self):
        self.inventory_images.nth(0).click()



