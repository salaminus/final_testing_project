from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверка на корректный url адрес

        print('*' * 10, self.browser.current_url)
        assert 'login' in self.url

    def should_be_login_form(self):
        # проверка, что есть форма логина
        assert LoginPageLocators.LOGIN_FORM

    def should_be_register_form(self):
        # проверка, что есть форма регистрации на странице
        assert LoginPageLocators.REG_FORM