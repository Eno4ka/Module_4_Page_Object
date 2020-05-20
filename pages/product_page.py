from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_product_to_basket(self):
        button = self.browser.find_element_by_css_selector(".btn.btn-lg.btn-primary")
        button.click()

    def should_be_button_add_to_basket(self):
        assert self.browser.find_element_by_css_selector(*ProductPageLocators.BUTTON), "Button ADD TO BASKET NOT FOUND"