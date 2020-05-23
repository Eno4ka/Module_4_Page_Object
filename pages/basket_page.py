from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators, BASKET_EMPTY), "Basket not empty"
        basket_empty = self.browser.find_element(*BasketPageLocators, BASKET_EMPTY).text
        assert "emrty" in basket_empty, "The basket not empty"