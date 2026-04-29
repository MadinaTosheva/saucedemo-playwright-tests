from pages.base_page import BasePage
from pages.card_page import CardPage
from pages.inventory_page import InventoryPage


class DetailPage(InventoryPage):
    def __init__(self, page):
        super().__init__(page)