from src.app import App
from src.pages.android.catalog_page import CatalogPage
from src.tests.android.test_main_page import TestMainPage
from src.pages.android.main_page import MainPage
from src.pages.android.km_page import KMPage


class TestKMPage(TestMainPage):

    def __init__(self, driver):
        super().__init__(driver)

    def test_vidacha_rassrochka_title(self):
        """Проверяем отображение рассрочки на выдаче"""
        self.test_close_welcome_content()
        App.click(self, MainPage.navCatalog)
        App.click(self, CatalogPage.viewSearchAppBarLayoutContainer)
        App.send_keys(self, CatalogPage.viewSearchAppBarLayoutInput, 'Холодильники')
        App.click(self, CatalogPage.itemTitle)
        App.assert_text(self, CatalogPage.creditTitleView, 'Рассрочка')
        # App.assert_text(self, CatalogPage.creditView, '5 463 ₽')
        App.assert_contains_text(self, CatalogPage.creditView, '₽')
        # App.assert_text(self, CatalogPage.creditSmallView, '× 3 мес')
        App.assert_contains_text(self, CatalogPage.creditSmallView, 'мес')

    def test_km_rassrochka_vidget(self):
        """Проверяем отображение виджета Рассрочки от Тинькофф"""
        self.test_close_welcome_content()
        self.driver.execute_script("mobile: deepLink", {
            'url': 'https://market.yandex.ru/product--kholodilnik-atlant-khm-4208-000/10632003?sku=10632003&offerid=tYAB95YS6syrMUZe093BMQ',
            'package': 'ru.beru.android.qa'})
        App.swipe_x_y(self, locator='', start_x=500, start_y=700, count=2)
        App.assert_text(self, KMPage.installmentsTitleTextView, "Рассрочка от Тинькофф")
