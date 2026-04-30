from playwright.sync_api import expect

from pages.base_page import BasePage


class OverviewPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.item_quantity = self.page.locator(".cart_quantity")
        self.item_name = self.page.locator(".inventory_item_name")
        self.item_price = self.page.locator(".inventory_item_price")
        self.shipping_info = self.page.locator("//div[@class='summary_value_label'][2]")
        self.total_price = self.page.locator(".summary_subtotal_label")
        self.tax_amount = self.page.locator(".summary_tax_label")
        self.total_payment_amount = self.page.locator(".summary_total_label")
        self.finish_btn = self.page.locator("#finish")

    def validate_item_quantity(self, quantity):
        expect(self.item_quantity).to_have_text(quantity)

    def validate_item_name(self, item_name):
        expect(self.item_name).to_have_text(item_name)

    def validate_item_price(self, item_price):
        assert self.item_price.inner_text() == item_price

    def validate_shipping_info_text(self, text):
        expect(self.shipping_info).to_contain_text(text)

    def get_item_total(self):
        total_price = self.total_price.inner_text()
        price = total_price.split("$")[1]
        return price

    def get_tax(self):
        tax_price = self.tax_amount.inner_text()
        tax = tax_price.split("$")[1]
        return tax

    def validate_total_price(self, price):
        expect(self.total_price).to_contain_text(price)

    def validate_tax_amount(self, tax):
        expect(self.tax_amount).to_contain_text(tax)

    def validate_total_payment_amount(self, items_amount, tax_amount):
        item = float(items_amount)
        tax = float(tax_amount)

        total = item + tax
        rounded_total = f"{total:.2f}"
        print(rounded_total)
        expect(self.total_payment_amount).to_contain_text(rounded_total)

    def click_on_finish_btn(self):
        self.finish_btn.click()




