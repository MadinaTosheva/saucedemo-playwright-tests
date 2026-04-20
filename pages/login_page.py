from playwright.sync_api import expect

from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username_input = self.page.locator("#user-name")
        self.password_input = self.page.locator("#password")
        self.login_button = self.page.locator("#login-button")

    def enter_username(self, username):
        self.username_input.fill(username)

    def enter_password(self, password):
        self.password_input.fill(password)

    def click_login_btn(self):
        self.login_button.click()

    def validate_username(self, username):
        expect(self.username_input).to_have_value(username)

    def validate_password(self, password):
        expect(self.password_input).to_have_value(password)


