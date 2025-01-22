import time

from .base_page import BasePage
from .cart_page import CartPage
from .locators import ProductPageLocator

class ProductPage(BasePage):
    def should_be_add_product(self):
        self.name_product = self.browser.find_element(*ProductPageLocator.PRODUCT_NAME).text
        print(f"Название товара: {self.name_product}")
        self.browser.find_element(*ProductPageLocator.PRODUCT_ADD).click()
        # time.sleep(1)

    def should_go_cart(self):
        self.browser.find_element(*ProductPageLocator.CART_BUTTON).click()

    def should_name_product_in_cart(self):
        # name_product_in_cart = self.browser.find_element(*ProductPageLocator.NAME_PRODUCT_IN_CART).text
        # print(f"Название товара: {self.name_product}\n и в корзине:{name_product_in_cart}")
        # assert self.name_product == name_product_in_cart, \
        #     "Товары не совпали!!!"
        return CartPage(browser=self.browser, url=self.browser.current_url)