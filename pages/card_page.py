from playwright.sync_api import expect

from pages.base_page import BasePage


class CardPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.item_quantity = self.page.locator("[data-test='item-quantity']")

    def validate_item_quantity(self):
        expect(self.item_quantity).to_have_text("1")