from selenium.webdriver.common.by import By
# For selectors and locators

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocator():
    PRODUCT_ADD = (By.CSS_SELECTOR, "#add_to_basket_form")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    CART_BUTTON = (By.CSS_SELECTOR, ".btn-group > button.btn-default")


class CartProductLocator():
    NAME_PRODUCT_IN_CART = (By.CSS_SELECTOR, ".alert:nth-child(1) > .alertinner > strong")
    CART_PRICE = (By.CSS_SELECTOR, ".alertinner > p > strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
