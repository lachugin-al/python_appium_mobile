import pytest

from src.appium_setup import Driver
from src.pages.android.main_page import MainPage
from src.app import App


class TestMainPage(Driver):

    def __init__(self, driver):
        super().__init__(driver)

    def close_all_welcome_contents(self):
        while App.is_exist(self, MainPage.closeButton):
            App.click(self, MainPage.closeButton)

        while App.is_exist(self, MainPage.sliderIndicator):
            App.click(self, MainPage.sliderIndicator)

        if App.is_exist(self, MainPage.cookieContainer):
            if App.is_exist(self, MainPage.negativeButton):
                App.click(self, MainPage.negativeButton)

    def allert(self):
        App.click(self, MainPage.navCart)
        if App.is_exist(self, MainPage.allertTitle):
            App.assert_contains_text(self, MainPage.allertTitle, "Что-то пошло не так")
        else:
            self.logger.error("Аллерт не обнаружен")
