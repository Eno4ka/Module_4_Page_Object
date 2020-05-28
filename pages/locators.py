from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form.well")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form.well")
    EMAIL = (By.NAME, "registration-email")
    PASSWORD = (By.NAME, "registration-password1")
    PASSWORD_REPEAT = (By.NAME, "registration-password2")
    SUBMIT = (By.NAME, "registration_submit")

class ProductPageLocators():
    BUTTON_ADD = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary")
    NAME_PRODUCT = (By.CSS_SELECTOR, "#messages :nth-child(1) :nth-child(2) strong")
    NAME_PRODUCT_ADD = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    PRICE_ADD = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info.fade.in .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages :nth-child(1) :nth-child(2)")

class BasketPageLocators():
    BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_BTN = (By.CSS_SELECTOR, ".btn-group a.btn.btn-default")
    BASKET_PRODUCT = (By.CSS_SELECTOR, ".thumbnail")

