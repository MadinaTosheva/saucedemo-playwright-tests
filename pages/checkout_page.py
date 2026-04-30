import allure
from playwright.sync_api import expect

from pages.base_page import BasePage
from pages.login_page import LoginPage


class CheckoutPage(LoginPage):
    def __init__(self, page):
        super().__init__(page)
        self.firstname = self.page.locator("#first-name")
        self.lastname = self.page.locator("#last-name")
        self.postal_code = self.page.locator("#postal-code")
        self.continue_btn = self.page.locator("#continue")
        self.cancel = self.page.locator("#cancel")

    @allure.step("Enter firstname: '{firstname_}'")
    def enter_firstname(self, firstname_):
        self.firstname.fill(firstname_)

    @allure.step("Enter lastname: '{lastname_}'")
    def enter_lastname(self, lastname_):
        self.lastname.fill(lastname_)

    @allure.step("Enter postalcode: '{postalcode_}'")
    def enter_postalcode(self, postalcode_):
        self.postal_code.fill(postalcode_)

    @allure.step("Validate firstname: '{firstname_}'")
    def validate_firstname(self, firstname_):
        expect(self.firstname).to_have_value(firstname_)

    @allure.step("Validate lastname: '{lastname_}'")
    def validate_lastname(self, lastname_):
        expect(self.lastname).to_have_value(lastname_)

    @allure.step("Validate postalcode: '{postalcode_}'")
    def validate_postalcode(self, postalcode_):
        expect(self.postal_code).to_have_value(postalcode_)

    @allure.step("Click on continue button")
    def click_continue_btn(self):
        self.continue_btn.click()

    @allure.step("Click on cancel button")
    def click_cancel_btn(self):
        self.cancel.click()

    @allure.step("Make checkout process with (firstname: '{firstname_}, lastname: '{lastname_}', postalcode: '{postalcode_}')")
    def checkout_process(self, firstname_, lastname_, postalcode_):
        self.enter_firstname(firstname_)
        self.enter_lastname(lastname_)
        self.enter_postalcode(postalcode_)
        self.click_continue_btn()


