from src.appium_setup import Driver
from src.pages.android.main_page import MainPage
from src.app import App


class TestMainPage(Driver):

    def __init__(self, driver):
        super().__init__(driver)

    def test_close_all_welcome_contents(self):
        if App.is_exist(self, MainPage.welcomeContent):
            App.click(self, MainPage.closeButton)

        while App.is_exist(self, MainPage.sliderIndicator):
            App.click(self, MainPage.sliderIndicator)

        if App.is_exist(self, MainPage.cookieContainer):
            App.click(self, MainPage.negativeButton)


    def test_allert(self):
        self.test_close_welcome_content()
        App.click(self, MainPage.navCart)
        if App.is_exist(self, MainPage.allertTitle):
            App.assert_contains_text(self, MainPage.allertTitle, "Что-то пошло не так")
        else:
            self.logger.error("Аллерт не обнаружен")