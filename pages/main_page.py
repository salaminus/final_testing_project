import time

from selenium.webdriver.common.by import By
from .base_page import BasePage

from .locators import MainPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        time.sleep(2)


    def should_be_login_link(self):
        assert self.browser.find_element(*MainPageLocators.LOGIN_LINK)
