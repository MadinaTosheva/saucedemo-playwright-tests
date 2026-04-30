import allure
from playwright.sync_api import expect


class BasePage:

    def __init__(self, page):
        self.page = page

    @allure.step("Open page: '{path}'")
    def open_page(self, path):
        self.page.goto(path)

    @allure.step("Validate URL: '{path}'")
    def validate_url(self, path):
        expect(self.page).to_have_url(path)