from playwright.sync_api import expect

from config.products import SAUCE_LABS_BACKPACK_TEXT
from pages.base_page import BasePage


class InventoryPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.backpack = self.page.get_by_text(SAUCE_LABS_BACKPACK_TEXT)
        self.price = self.page.locator("(//div[@class='pricebar'])[1]/div[@class='inventory_item_price']")
        self.add_to_cart = self.page.locator("#add-to-cart-sauce-labs-backpack")
        self.remove = self.page.locator("#remove-sauce-labs-backpack")
        self.cart_badge = self.page.locator(".shopping_cart_badge")

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

