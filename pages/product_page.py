from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        button_add = self.browser.find_element(*ProductPageLocators.BUTTON_ADD)
        button_add.click()

    def name_book_matches(self):
        assert self.is_element_present(*ProductPageLocators.NAME_PRODUCT), "Product not found"
        assert self.is_element_present(*ProductPageLocators.NAME_PRODUCT_ADD), "Product not added"
        name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        name_product_add = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_ADD).text
        assert name_product == name_product_add, "The name product not added"
    def price_matches(self):
        assert self.is_element_present(*ProductPageLocators.PRICE), "The price of product not found"
        assert self.is_element_present(*ProductPageLocators.PRICE_ADD), "The price added of product not found"
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        price_add = self.browser.find_element(*ProductPageLocators.PRICE_ADD).text
        assert price == price_add, "Price not matches"

    def should_be_url(self):
        failed_url = self.browser.current_url
        print(failed_url)
        assert failed_url, "URL не существует"