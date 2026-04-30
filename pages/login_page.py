import allure
from playwright.sync_api import expect

from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username_input = self.page.locator("#user-name")
        self.password_input = self.page.locator("#password")
        self.login_button = self.page.locator("#login-button")
        self.error = self.page.locator(".error-message-container h3")

    @allure.step("Enter username: '{username}'")
    def enter_username(self, username):
        self.username_input.fill(username)

    @allure.step("Enter password: '{password}'")
    def enter_password(self, password):
        self.password_input.fill(password)

    @allure.step("Click on login button")
    def click_login_btn(self):
        self.login_button.click()

    @allure.step("Validate username field value is '{username}'")
    def validate_username(self, username):
        expect(self.username_input).to_have_value(username)

    @allure.step("Validate password field value is '{password}'")
    def validate_password(self, password):
        expect(self.password_input).to_have_value(password)

    @allure.step("Validate error message is visible")
    def validate_visibility_of_error(self):
        expect(self.error).to_be_visible()

    @allure.step("Validate error text is: '{error_text}'")
    def validate_error_text(self, error_text):
        expect(self.error).to_have_text(error_text)

    @allure.step("Login with username: '{username_}' and password: '{password_}'")
    def login_process(self, username_, password_):
        self.enter_username(username_)
        self.enter_password(password_)
        self.click_login_btn()

    @allure.step("Check error message: '{error_text}'")
    def error_check(self, error_text):
        self.validate_visibility_of_error()
        self.validate_error_text(error_text)
