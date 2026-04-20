from playwright.sync_api import expect


class BasePage:

    def __init__(self, page):
        self.page = page

    def open_page(self, path):
        self.page.goto(path)

    def validate_url(self, path):
        expect(self.page).to_have_url(path)