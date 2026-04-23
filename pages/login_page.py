from playwright.sync_api import expect

from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username_input = self.page.locator("#user-name")
        self.password_input = self.page.locator("#password")
        self.login_button = self.page.locator("#login-button")
        self.error = self.page.locator(".error-message-container h3")

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

    def validate_visibility_of_error(self):
        expect(self.error).to_be_visible()

    def validate_error_text(self, error_text):
        expect(self.error).to_have_text(error_text)

    def login_procedure(self, username_, password_):
        self.enter_username(username_)
        self.enter_password(password_)
        self.click_login_btn()

    def error_check(self, error_text):
        self.validate_visibility_of_error()
        self.validate_error_text(error_text)
