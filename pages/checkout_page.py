from playwright.sync_api import expect

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.firstname = self.page.locator("#first-name")
        self.lastname = self.page.locator("#last-name")
        self.postal_code = self.page.locator("#postal-code")
        self.continue_btn = self.page.locator("#continue")

    def enter_firstname(self, firstname_):
        self.firstname.fill(firstname_)

    def enter_lastname(self, lastname_):
        self.lastname.fill(lastname_)

    def enter_postalcode(self, postalcode_):
        self.postal_code.fill(postalcode_)

    def validate_firstname(self, firstname_):
        expect(self.firstname).to_have_value(firstname_)

    def validate_lastname(self, lastname_):
        expect(self.lastname).to_have_value(lastname_)

    def validate_postalcode(self, postalcode_):
        expect(self.postal_code).to_have_value(postalcode_)

    def click_continue_btn(self):
        self.continue_btn.click()


