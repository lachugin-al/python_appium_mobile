from src.app import App
from src.pages.android.catalog_page import CatalogPage
from src.tests.android.test_main_page import TestMainPage
from src.pages.android.main_page import MainPage
from src.pages.android.km_page import KMPage
from src.pages.android.checkouter_page import CheckouterPage


class TestKMPage(TestMainPage):

    def __init__(self, driver):
        super().__init__(driver)

    def test_vidacha_rassrochka_title(self):
        """
        Проверяем отображение лейбла 00Х
        Рассрочки в байбоксе
        """
        self.test_close_welcome_content()
        App.click(self, MainPage.navCatalog)
        App.click(self, CatalogPage.viewSearchAppBarLayoutContainer)
        App.send_keys(self, CatalogPage.viewSearchAppBarLayoutInput, "Холодильники")
        App.click(self, CatalogPage.itemTitle)
        App.assert_contains_text(self, CatalogPage.itemTitle, "Холодильник")
        App.swipe_x_y(self, locator="", start_x=500, start_y=700, count=1)
        App.is_displayed(self, CatalogPage.installmentGroupView)
        App.assert_text(self, CatalogPage.installmentTitle, "РАССРОЧКА")
        App.assert_text(self, CatalogPage.installmentFirstPeriod, "0")
        App.assert_text(self, CatalogPage.installmentSecondPeriod, "0")
        App.assert_text(self, CatalogPage.installmentThirdPeriod, "3")
        App.assert_text(self, CatalogPage.creditTitleView, "Рассрочка")
        App.assert_contains_text(self, CatalogPage.creditView, "₽")
        App.assert_text(self, CatalogPage.creditSmallView, '× 3 мес')
        # App.assert_contains_text(self, CatalogPage.creditSmallView, "мес")

    def test_km_rassrochka_vidget(self):
        """
        Проверяем отображение виджета Рассрочки от Тинькофф
        Переход по кнопке Оформить
        """
        self.test_close_welcome_content()
        self.driver.execute_script("mobile: deepLink", {
            "url": "https://market.yandex.ru/product--kholodilnik-atlant-khm-4208-000/10632003?sku=10632003&offerid=tYAB95YS6syrMUZe093BMQ",
            "package": "ru.beru.android.qa"})
        App.swipe_x_y(self, locator='', start_x=500, start_y=500, count=1)
        App.is_displayed(self, KMPage.offerInstallmentsBlock)
        App.assert_text(self, KMPage.installmentsTitleTextView, "Рассрочка от Тинькофф")
        App.is_displayed(self, KMPage.installmentsTermView)
        App.assert_contains_text(self, KMPage.onePeriodTextView, "мес")
        App.assert_contains_text(self, KMPage.monthlyPayment, "₽")
        App.is_displayed(self, KMPage.installmentsOrderButton)
        # Добавить проверку рассрочки в компакном оффере
        App.click(self, KMPage.installmentsOrderButton)
        App.assert_text(self, CheckouterPage.toolbarText, "Оформление заказа")
