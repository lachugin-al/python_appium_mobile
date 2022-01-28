from selenium.webdriver.common.by import By

from src.appium_setup import Driver
from src.pages.android.catalog_page import CatalogPage
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
        flag = App.is_exist(self, MainPage.cookieContainer)
        if flag:
            App.click(self, MainPage.negativeButton)

    def test_vidacha_credit_title(self):
        self.test_welcome_content()
        App.click(self, MainPage.navCatalog)
        App.click(self, CatalogPage.viewSearchAppBarLayoutContainer)
        App.send_keys(self, CatalogPage.viewSearchAppBarLayoutInput, 'Холодильники')
        App.click(self, CatalogPage.itemTitle)
        App.assert_text(self, CatalogPage.creditTitleView, 'Рассрочка')
        App.assert_text(self, CatalogPage.creditView, '5 463 ₽')
        App.assert_text(self, CatalogPage.creditSmallView, '× 3 мес')