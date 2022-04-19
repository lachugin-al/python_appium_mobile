import time

from src.app import App
from src.appium_setup import Driver
from src.tests.android.fintech.test_main_page import TestMainPage
from src.pages.android.main_page import MainPage
from src.pages.android.km_page import KMPage


class TestCartPage(Driver):

    def __init__(self, driver):
        super().__init__(driver)

    def test_3_vijets_in_cart(self):
        """Проверка наличия и отображения 3х виджетов в корзине"""

        # self.close_all_welcome_contents()
        self.driver.execute_script("mobile: deepLink", {
            "url": "yamarket://product--cinetic-big-ball-animal-pro-2/515571001?sku=100868870241&offerid=3G7T1VT2MrMs6k59eZdmoQ",
            "package": "ru.beru.android.qa"})
        time.sleep(10)
        App.swipe_x_y(self, locator='', start_x=500, start_y=700, count=2)
        flag = App.is_exist(self, KMPage.cartMinusButton)  # есть товар в корзине
        while flag:
            App.click(self, KMPage.cartMinusButton)
            time.sleep(2)
            flag = App.is_exist(self, KMPage.cartMinusButton)
        App.click(self, KMPage.cartCounterButton)
        if App.is_exist(self, MainPage.sliderIndicator):
            App.click(self, MainPage.sliderIndicator)
        App.click(self, MainPage.navCart)
        time.sleep(10)
        App.swipe_x_y(self, locator='', start_x=500, start_y=700, count=2)

        # проверяем бнпл виджет
        App.is_displayed(self, KMPage.offerBnplBlock)
        App.assert_contains_text(self, KMPage.bnplBlockInitSum, "сегодня")
        App.assert_contains_text(self, KMPage.bnplBlockMonthSum, "потом, без переплат")
        App.is_displayed(self, KMPage.proceedBnpl)
        App.is_displayed(self, KMPage.bnplTableView)
        App.is_displayed(self, KMPage.firstPayment)
        App.is_displayed(self, KMPage.secondPayment)
        App.is_displayed(self, KMPage.thirdPayment)
        App.is_displayed(self, KMPage.firthPayment)
        App.assert_contains_text(self, KMPage.firstDateTextView, " ")
        App.assert_contains_text(self, KMPage.secondDateTextView, " ")
        App.assert_contains_text(self, KMPage.thirdDateTextView, " ")
        App.assert_contains_text(self, KMPage.fourthDateTextView, " ")
        App.assert_contains_text(self, KMPage.firstAmountTextView, "₽")
        App.assert_contains_text(self, KMPage.secondAmountTextView, "₽")
        App.assert_contains_text(self, KMPage.thirdAmountTextView, "₽")
        App.assert_contains_text(self, KMPage.fourthAmountTextView, "₽")
        App.assert_text(self, KMPage.moreInfoTextView, "Подробнее")

        # проверяем кредитный виджет
        App.is_displayed(self, KMPage.offerCreditBlock)
        App.assert_text(self, KMPage.cartTinkoffCreditBlockTitle, "Кредит от Тинькофф")
        App.assert_contains_text(self, KMPage.cartTinkoffCreditBlockMonthPayment, "₽")
        App.is_displayed(self, KMPage.proceedCredit)
        App.assert_contains_text(self, KMPage.creditPriceView, "₽")

        # TODO - проверка виджета Рассрочки
