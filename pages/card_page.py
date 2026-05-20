import allure
from playwright.sync_api import expect

from pages.base_page import BasePage


class CardPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.item_quantity = self.page.locator("[data-test='item-quantity']")
        self.inventory_item_name = self.page.locator(".inventory_item_name")
        self.cart_price = self.page.locator(".inventory_item_price")
        self.checkout_btn = self.page.locator("#checkout")
        self.continue_shopping_btn = self.page.locator("#continue-shopping")

    @allure.step("Validate item quantity is '{value}'")
    def validate_item_quantity(self, value: str = "1"):
        expect(self.item_quantity).to_have_text(value)

    @allure.step("Validate product name is '{product_name}'")
    def validate_product_name(self, product_name: str):
        expect(self.inventory_item_name).to_contain_text(product_name)

    @allure.step("Validate product price is '{saved_price}'")
    def validate_product_price(self, saved_price):
        assert self.cart_price.inner_text() == saved_price

    @allure.step("Click on checkout button")
    def click_on_checkout_btn(self):
        self.checkout_btn.click()

    @allure.step("Click on continue shopping button")
    def click_on_continue_shopping(self):
        self.continue_shopping_btn.click()

    @allure.step("Validate card badge is empty")
    def validate_cart_badge_is_empty(self):
        expect(self.inventory_item_name).to_have_count(0)
