import allure
from playwright.sync_api import expect

from pages.base_page import BasePage


class CompletePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.complete_title = self.page.locator(".title")
        self.complete_header = self.page.locator('.complete-header')
        self.complete_text = self.page.locator(".complete-text")
        self.back_home_btn = self.page.locator("#back-to-products")

    @allure.step("Validate title: '{title_}'")
    def validate_title(self, title_):
        expect(self.complete_title).to_have_text(title_)

    @allure.step("Validate header text: '{header_text}'")
    def validate_header_text(self, header_text):
        expect(self.complete_header).to_have_text(header_text)

    @allure.step("Validate complete text: '{complete_text}'")
    def validate_complete_text(self, complete_text):
        expect(self.complete_text).to_contain_text(complete_text)

    @allure.step("Validate button is enabled")
    def button_enabled(self):
        expect(self.back_home_btn).to_be_enabled()

    @allure.step("Click on back home button")
    def click_on_back_home_btn(self):
        self.back_home_btn.click()
