from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form.well")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form.well")

class ProductPageLocators():
    BUTTON_ADD = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary")
    NAME_PRODUCT = (By.CSS_SELECTOR, "#messages :nth-child(1) :nth-child(2) strong")
    NAME_PRODUCT_ADD = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    PRICE_ADD = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info.fade.in .alertinner strong")