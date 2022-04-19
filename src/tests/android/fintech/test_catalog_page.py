import time

from src.app import App
from src.appium_setup import Driver
from src.pages.android.catalog_page import CatalogPage
from src.tests.android.fintech.test_main_page import TestMainPage


class TestCatalogPage(Driver):

    def __init__(self, driver):
        super().__init__(driver)

    def test_catalog_installments_testing(self):
        """Тест на Выдачу отображение Рассрочки на 6 мес"""
        # self.close_all_welcome_contents()
        self.driver.execute_script("mobile: deepLink", {
            "url": "yamarket://catalog--podushki-i-kresla-dlia-kormleniia/16418175/list?text=Body%20Pillow%20U&cpa=1&hid=10752772&pricefrom=3000&onstock=0&local-offers-first=0",
            "package": "ru.beru.android.qa"})
        time.sleep(10)
        App.swipe_x_y(self, locator='', start_x=500, start_y=700, count=2)
        App.is_displayed(self, CatalogPage.creditContainer)
        App.assert_text(self, CatalogPage.creditTitleView, "Рассрочка")
        App.assert_contains_text(self, CatalogPage.creditView, "₽")
        App.assert_text(self, CatalogPage.creditSmallView, '× 6 мес')

    def test_catalog_credit_testing(self):
        """Тест на Выдачу отображение Кредита от Тинькофф"""
        # self.close_all_welcome_contents()
        self.driver.execute_script("mobile: deepLink", {
            "url": "yamarket://catalog--komplekty-klaviatur-i-myshei/26913150/list?text=Defender%20Target%20MKP-350&cpa=1&hid=723088&onstock=0&local-offers-first=0",
            "package": "ru.beru.android.qa"})
        time.sleep(10)
        App.is_displayed(self, CatalogPage.creditContainer)
        App.assert_text(self, CatalogPage.creditViewTitle, "Кредит")
        App.is_displayed(self, CatalogPage.creditViewLayout)
        App.assert_contains_text(self, CatalogPage.creditView, "₽")

    def test_catalog_bnpl_testing(self):
        """Тест на Выдачу отображение БНПЛ"""
        # self.close_all_welcome_contents()
        self.driver.execute_script("mobile: deepLink", {
            "url": "yamarket://catalog--detskie-tovary/54421/list?text=happy-baby-smiley-v2&cpa=1&hid=90764&onstock=0&local-offers-first=0",
            "package": "ru.beru.android.qa"})
        time.sleep(10)
        App.swipe_x_y(self, locator='', start_x=500, start_y=700, count=2)
        App.is_displayed(self, CatalogPage.creditContainer)
        App.assert_text(self, CatalogPage.creditViewTitle, "Оплата частями")


    def test_catalog_bnpl_prod(self):
        """Поиск лейбла бнпл на выдаче через диплинк"""
        self.driver.execute_script("mobile: deepLink", {
        "url": "yamarket://catalog--umnye-kolonki/26992350/list?glfilter=7893318%3A15562112&text=яндекс%20станция&cpa=1&hid=15553892&rs=eJwzYgpgBAABcwCG&was_redir=1&rt=10&onstock=0&local-offers-first=0",
        "package": "ru.beru.android.qa"})
        time.sleep(15)
        App.swipe_x_y(self, locator='', start_x=500, start_y=590, count=1)
        App.is_displayed(self, CatalogPage.creditContainer)
        App.assert_text(self, CatalogPage.creditViewTitle, "Оплата частями")

    def test_catalog_bnpl_prod2(self):
        """Поиск лейбла бнпл на выдаче через диплинк"""
        self.driver.execute_script("mobile: deepLink", {
            "url": "yamarket://catalog--umnye-kolonki/26992350/list?glfilter=7893318%3A15562112&text=яндекс%20станция&cpa=1&hid=15553892&rs=eJwzYgpgBAABcwCG&was_redir=1&rt=10&onstock=0&local-offers-first=0",
            "package": "ru.beru.android.qa"})
        time.sleep(15)
        App.swipe_x_y(self, locator='', start_x=500, start_y=600, count=1)
        App.is_displayed(self, CatalogPage.creditContainer)
        App.assert_text(self, CatalogPage.creditViewTitle, "Не Оплата частями")
