from .pages.main_page import MainPage
from selenium.webdriver.common.by import By

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    # page.go_to_login_page()
    page.should_be_login_link()



# run:
# pytest.exe -v --tb=line test_main_page.py