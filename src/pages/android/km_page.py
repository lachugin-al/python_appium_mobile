from appium.webdriver.common.mobileby import MobileBy
from src.appium_setup import Driver


class KMPage(Driver):
    """
    карточка моделм/оффера
    """

    productSummaryTitleView = (MobileBy.ID, "ru.beru.android.qa:id/productSummaryTitleView")

    # КМ товара
    pricesPriceBnplTextView = (MobileBy.ID, "ru.beru.android.qa:id/pricesPriceBnplTextView") # или частями около цены
    productMainCartButton = (MobileBy.ID, "ru.beru.android.qa:id/productMainCartButton") # кнопка Добавить в корзину

    # Виджет BNPL
    offerBnplBlock = (MobileBy.ID, "ru.beru.android.qa:id/offerBnplBlock") # виджет
    bnplBlockInitSum = (MobileBy.ID, "ru.beru.android.qa:id/bnplBlockInitSum") # * сегодня
    bnplBlockMonthSum = (MobileBy.ID, "ru.beru.android.qa:id/bnplBlockMonthSum") # и * потом, без переплат
    proceedBnpl = (MobileBy.ID, "ru.beru.android.qa:id/proceedBnpl") # оформить
    bnplTableView = (MobileBy.ID, "ru.beru.android.qa:id/bnplTableView") # график
    firstPayment = (MobileBy.ID, "ru.beru.android.qa:id/firstPayment") # колбаска1
    secondPayment = (MobileBy.ID, "ru.beru.android.qa:id/secondPayment") # колбаска2
    third_payment = (MobileBy.ID, "ru.beru.android.qa:id/third_payment") # колбаска3
    firth_payment = (MobileBy.ID, "ru.beru.android.qa:id/firth_payment") # колбаска4
    firstDateTextView = (MobileBy.ID, "ru.beru.android.qa:id/firstDateTextView") # дата 1 платежа
    secondDateTextView = (MobileBy.ID, "ru.beru.android.qa:id/secondDateTextView") # дата 2 платежа
    thirdDateTextView = (MobileBy.ID, "ru.beru.android.qa:id/thirdDateTextView") # дата 3 платежа
    fourthDateTextView = (MobileBy.ID, "ru.beru.android.qa:id/fourthDateTextView") # дата 4 платежа
    firstAmountTextView = (MobileBy.ID, "ru.beru.android.qa:id/firstAmountTextView") # сумма 1 платежа
    secondAmountTextView = (MobileBy.ID, "ru.beru.android.qa:id/secondAmountTextView") # сумма 2 платежа
    thirdAmountTextView = (MobileBy.ID, "ru.beru.android.qa:id/thirdAmountTextView") # сумма 3 платежа
    fourthAmountTextView = (MobileBy.ID, "ru.beru.android.qa:id/fourthAmountTextView") # сумма 4 платежа
    moreInfoTextView = (MobileBy.ID, "ru.beru.android.qa:id/moreInfoTextView") # подробнее
    moreInfoTextViewAfterOpen = (MobileBy.XPATH,
                                 "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView")

    # Виджет Рассрочки
    offerInstallmentsBlock = (MobileBy.ID, "ru.beru.android.qa:id/offerInstallmentsBlock") # виджет
    installmentsTitleTextView = (MobileBy.ID, "ru.beru.android.qa:id/installmentsTitleTextView") # 	Рассрочка от Тинькофф
    installmentsTermView = (MobileBy.ID, "ru.beru.android.qa:id/installmentsTermView") # блок на 3 мес = ... ₽/мес
    onePeriodTextView = (MobileBy.ID, "ru.beru.android.qa:id/onePeriodTextView") # 3 мес
    monthlyPayment = (MobileBy.ID, "ru.beru.android.qa:id/monthlyPayment") # ... ₽/мес
    installmentsOrderButton = (MobileBy.ID, "ru.beru.android.qa:id/installmentsOrderButton") # Оформить

    # Виджет Кредита
    offerCreditBlock = (MobileBy.ID, "ru.beru.android.qa:id/offerCreditBlock") # виджет
    cartTinkoffCreditBlockTitle = (MobileBy.ID, "ru.beru.android.qa:id/cartTinkoffCreditBlockTitle") # Кредит от Тинькофф
    cartTinkoffCreditBlockMonthPayment = (MobileBy.ID, "ru.beru.android.qa:id/cartTinkoffCreditBlockMonthPayment") # от ... ₽ / мес.
    proceed_credit = (MobileBy.ID, "ru.beru.android.qa:id/proceed_credit") # Оформить

    # Хэддер
    pricesContainer = (MobileBy.ID, "ru.beru.android.qa:id/pricesContainer")
    pricesBasePriceView = (MobileBy.ID, "ru.beru.android.qa:id/pricesBasePriceView")
    pricesPriceView = (MobileBy.ID, "ru.beru.android.qa:id/pricesPriceView")
    creditPriceView = (MobileBy.ID, "ru.beru.android.qa:id/creditPriceView") # от ... ₽ / мес. в компактном оффере [@index = 1]
    cartCounterButton = (MobileBy.ID, "ru.beru.android.qa:id/cartCounterButton")

    def __init__(self, driver):
        super().__init__(driver)
