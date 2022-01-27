from src.appium_setup import Driver
from src.pages.android.main_page import MainPage
from src.app import App


class TestWelcome(Driver):

    def __init__(self, driver):
        super().__init__(driver)

    def test_welcome_content(self):
        flag = App.is_exist(self, MainPage.welcomeContent)
        if flag:
            App.click(self, MainPage.closeButton)

        flag = App.is_exist(self, MainPage.sliderIndicator)
        if flag:
            App.click(self, MainPage.sliderIndicator)
