from .base_page import BasePage
from .locators import CartProductLocator

class CartPage(BasePage):
    def should_be_added_product(self):
        self.product_name = self.browser.find_element(*CartProductLocator.NAME_PRODUCT_IN_CART).text
        # print('*' * 10, self.product_name)
        return self.product_name

    def should_price_product_and_cart(self):
        price_product = self.browser.find_element(*CartProductLocator.PRODUCT_PRICE).text
        price_cart = self.browser.find_element(*CartProductLocator.PRODUCT_PRICE).text
        assert price_cart == price_product, "Цена корзины и товара не совпадают!!!"