from playwright.sync_api import expect

from config.products import SAUCE_LABS_BACKPACK
from pages.base_page import BasePage


class CardPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.item_quantity = self.page.locator("[data-test='item-quantity']")
        self.inventory_item_name = self.page.locator(".inventory_item_name")
        self.cart_price = self.page.locator(".inventory_item_price")
        self.checkout_btn = self.page.locator("#checkout")
        self.continue_shopping_btn = self.page.locator("#continue-shopping")

    def validate_item_quantity(self):
        expect(self.item_quantity).to_have_text("1")

    def validate_product_name(self):
        expect(self.inventory_item_name).to_contain_text(SAUCE_LABS_BACKPACK)

    def validate_product_price(self, saved_price):
        assert self.cart_price.inner_text() == saved_price

    def click_on_checkout_btn(self):
        self.checkout_btn.click()

    def click_on_continue_shopping(self):
        self.continue_shopping_btn.click()

    def validate_cart_badge_is_empty(self):
        expect(self.inventory_item_name).to_have_count(0)