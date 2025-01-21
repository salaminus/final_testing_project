from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from selenium.webdriver.common.by import By

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    # login_link = 'https://selenium1py.pythonanywhere.com/ru/accounts/login/'
    page = MainPage(browser, link)
    page.open()
    login_page = page.go_to_login_page()
    login_page.should_be_login_page()
    # Or (Into the MainPage need delete return!!!):
    # login_page = LoginPage(browser, browser.current_url)
    # login_page.should_be_login_page()

    # Old:
    # page.go_to_login_page()
    # page.should_be_login_link()
    # login_page = LoginPage(browser, login_link)
    # login_page.should_be_login_url()
    # login_page.should_be_login_form()
    # login_page.should_be_register_form()


# run:
# pytest.exe -v --tb=line test_main_page.py