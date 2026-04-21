from playwright.sync_api import expect

from config.products import SAUCE_LABS_BACKPACK_TEXT
from pages.base_page import BasePage


class CardPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.item_quantity = self.page.locator("[data-test='item-quantity']")
        self.backpack = self.page.locator(".inventory_item_name")
        self.cart_price = self.page.locator(".inventory_item_price")
        self.checkout_btn = self.page.locator("#checkout")

    def validate_item_quantity(self):
        expect(self.item_quantity).to_have_text("1")

    def validate_product_name(self):
        expect(self.backpack).to_contain_text(SAUCE_LABS_BACKPACK_TEXT)

    def validate_product_price(self, saved_price):
        assert self.cart_price.inner_text() == saved_price

    def click_on_checkout_btn(self):
        self.checkout_btn.click()


