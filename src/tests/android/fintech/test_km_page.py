import time

from src.app import App
from src.appium_setup import Driver
from src.tests.android.fintech.test_main_page import TestMainPage
from src.pages.android.km_page import KMPage


class TestKMPage(Driver):

    def __init__(self, driver):
        super().__init__(driver)

    def km_installments_and_credit_2_vidjets_testing(self):
        """
        Тест на КМ отображение 2х виджетов Рассрочка 3 или 6 мес и Кредит
        """
        self.driver.execute_script("mobile: deepLink", {
            "url": "yamarket://product--podushka-body-pillow-u-khollofaiber/1722620568?sku=100126176323&offerid=Wk5TKm_8jUbl48gPoZookw",
            "package": "ru.beru.android.qa"})
        time.sleep(10)
        App.swipe_x_y(self, locator='', start_x=500, start_y=700, count=2)
        App.is_displayed(self, KMPage.offerInstallmentsBlock)
        App.assert_text(self, KMPage.installmentsTitleTextView, "Рассрочка от Тинькофф")
        App.is_displayed(self, KMPage.installmentsTermView)
        App.assert_contains_text(self, KMPage.onePeriodTextView, "6")
        App.assert_contains_text(self, KMPage.monthlyPayment, "₽")
        App.is_displayed(self, KMPage.installmentsOrderButton)
        App.is_displayed(self, KMPage.offerCreditBlock)
        App.assert_text(self, KMPage.cartTinkoffCreditBlockTitle, "Кредит от Тинькофф")
        App.assert_contains_text(self, KMPage.cartTinkoffCreditBlockMonthPayment, "₽")
        App.is_displayed(self, KMPage.proceedCredit)
        App.assert_contains_text(self, KMPage.creditPriceView, "₽")

    def km_installments_baraban(self):
        """
        Тест на КМ отображение виджета Рассрочки с барабаном
        изменение состояний барабана и данных на компактном оффере
        вызов поп-ап барабана
        """
        self.driver.execute_script("mobile: deepLink", {
            "url": "yamarket://product--vstraivaemaia-posudomoechnaia-mashina-samsung-dw60m9550us/71335995?sku=71335995&offerid=Cmxk2TCHAUGgSmFPyQxQAA",
            "package": "ru.beru.android.qa"})
        time.sleep(10)
        App.swipe_x_y(self, locator='', start_x=500, start_y=700, count=2)
        App.is_displayed(self, KMPage.offerInstallmentsBlock)
        App.assert_text(self, KMPage.installmentsTitleTextView, "Рассрочка от Тинькофф")
        App.is_displayed(self, KMPage.internalNumberPicker)
        App.assert_contains_text(self, KMPage.monthlyPayment, "1 389 ₽")
        App.is_displayed(self, KMPage.installmentsOrderButton)
        App.click(self, KMPage.picker)
        App.is_displayed(self, KMPage.design_bottom_sheet)
        App.assert_text(self, KMPage.orderId, "Выберите срок рассрочки")
        App.is_displayed(self, KMPage.rootContainer1)
        App.assert_text(self, KMPage.periodTitle1, "3 мес")
        App.assert_contains_text(self, KMPage.periodPrice1, "по 11 111 ₽")
        App.is_displayed(self, KMPage.rootContainer2)
        App.assert_text(self, KMPage.periodTitle2, "6 мес")
        App.assert_contains_text(self, KMPage.periodPrice2, "по 5 556 ₽")
        App.is_displayed(self, KMPage.rootContainer3)
        App.assert_text(self, KMPage.periodTitle3, "12 мес")
        App.assert_contains_text(self, KMPage.periodPrice3, "по 2 778 ₽")
        App.is_displayed(self, KMPage.rootContainer4)
        App.assert_text(self, KMPage.periodTitle4, "24 мес")
        App.assert_contains_text(self, KMPage.periodPrice4, "по 1 389 ₽")
        App.click(self, KMPage.rootContainer1)
        App.click(self, KMPage.okButton)
        App.assert_contains_text(self, KMPage.monthlyPayment, "11 111 ₽")
        App.swipe_x_y(self, locator='', start_x=240, start_y=1340, end_x=240, end_y=1310, count=1)
        App.assert_contains_text(self, KMPage.monthlyPayment, "5 556 ₽")
        App.swipe_x_y(self, locator='', start_x=240, start_y=1340, end_x=240, end_y=1310, count=1)
        App.assert_contains_text(self, KMPage.monthlyPayment, "2 778 ₽")
        App.swipe_x_y(self, locator='', start_x=240, start_y=1340, end_x=240, end_y=1310, count=1)
        App.assert_contains_text(self, KMPage.monthlyPayment, "1 389 ₽")

    def test_km_bnpl_vijet_prod(self):
        """
        Тест на КМ отображение виджета БНПЛ
        """
        self.driver.execute_script("mobile: deepLink", {
            "url": "yamarket://product--kholodilnik-atlant-kh-2401-100/1725046033?sku=1725046033&offerid=4mWu-WkwB7718qTf1-TwAg",
            "package": "ru.beru.android.qa"})
        time.sleep(10)
        App.swipe_x_y(self, locator='', start_x=500, start_y=680, count=1)
        App.assert_text(self, KMPage.pricesPriceBnplTextView, "или частями")
        App.swipe_x_y(self, locator='', start_x=500, start_y=680, count=1)
        App.is_displayed(self, KMPage.offerBnplBlock)
        App.assert_contains_text(self, KMPage.bnplBlockInitSum, "сегодня")
        App.assert_contains_text(self, KMPage.bnplBlockMonthSum, "потом")
        App.is_displayed(self, KMPage.proceedBnpl)
        App.is_displayed(self, KMPage.bnplPaymentsTableView)
        App.is_displayed(self, KMPage.firstTableItem)
        App.is_displayed(self, KMPage.paymentPeriodIcon)
        App.assert_contains_text(self, KMPage.dateTextView, "апр")
        App.assert_contains_text(self, KMPage.amountTextView, "₽")
        App.is_displayed(self, KMPage.secondTableItem)
        App.is_displayed(self, KMPage.thirdTableItem)
        App.is_displayed(self, KMPage.fourthTableItem)
        App.assert_contains_text(self, KMPage.commissionTextView, "Без переплат")
        App.assert_text(self, KMPage.moreInfoTextView, "Подробнее")
        App.click(self, KMPage.moreInfoTextView)
        time.sleep(5)
        App.assert_contains_text(self, KMPage.moreInfoTextViewAfterOpen, "Оплата покупок частями")
