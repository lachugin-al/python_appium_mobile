from src.appium_setup import Driver
from src.pages.android.main_page import MainPage
from src.app import App


class TestWelcome(Driver):

    def __init__(self, driver):
        super().__init__(driver)

    def test_welcome_content(self):
        if App.element(self, MainPage.welcomeContent):
            App.click(self, MainPage.closeButton)
        if App.element(self, MainPage.coupon_slider):
            App.click(self, MainPage.coupon_slider)
