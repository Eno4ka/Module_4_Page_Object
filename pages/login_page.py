from .base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        self.url = self.url.current_url(By.CSS_SELECTOR, "#login_link[href="ru/accounts/login/"]")
        assert True, "URL не существует"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        self.login_form = self.login_form.find_element(By.CSS_SELECTOR, "#login_form.well")
        assert True, "Login_form отсутствует"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        self.register_form = self.register_form.find_element(By.CSS_SELECTOR, "#register_form.well")
        assert True, "Register_form отсутствует"