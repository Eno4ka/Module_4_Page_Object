from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), "Basket not empty"
        basket_empty = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY).text
        assert basket_empty is not None, "The basket not empty"

    def basket_with_product(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCT), "The product in basket"
