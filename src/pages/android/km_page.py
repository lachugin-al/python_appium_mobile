from appium.webdriver.common.mobileby import MobileBy
from src.appium_setup import Driver


class KMPage(Driver):
    """
    Карточка модели/оффера
    """

    productSummaryTitleView = (MobileBy.ID, "ru.beru.android.qa:id/productSummaryTitleView")

    # КМ товара
    pricesPriceBnplTextView = (MobileBy.ID, "ru.beru.android.qa:id/pricesPriceBnplTextView")  # или частями около цены
    productMainCartButton = (MobileBy.ID, "ru.beru.android.qa:id/productMainCartButton")  # кнопка Добавить в корзину
    cartButtonProgressButton = (
        MobileBy.ID, "ru.beru.android.qa:id/cartButtonProgressButton")  # значение кнопки Добавить в корзину
    cartMinusButton = (MobileBy.ID, "ru.beru.android.qa:id/cartMinusButton")  # -
    cartPlusButton = (MobileBy.ID, "ru.beru.android.qa:id/cartPlusButton")  # +

    # Виджет BNPL
    offerBnplBlock = (MobileBy.ID, "ru.beru.android.qa:id/offerBnplBlock")  # виджет
    bnplBlockInitSum = (MobileBy.ID, "ru.beru.android.qa:id/bnplBlockInitSum")  # * сегодня
    bnplBlockMonthSum = (MobileBy.ID, "ru.beru.android.qa:id/bnplBlockMonthSum")  # и * потом, без переплат
    proceedBnpl = (MobileBy.ID, "ru.beru.android.qa:id/proceedBnpl")  # оформить
    bnplPaymentsTableView = (MobileBy.ID, "ru.beru.android.qa:id/bnplPaymentsTableView")  # график
    commissionTextView = (MobileBy.ID, "ru.beru.android.qa:id/commissionTextView")  # Без переплат

    firstTableItem = (MobileBy.ID, "ru.beru.android.qa:id/firstTableItem")  # первый блок графика
    paymentPeriodIcon = (MobileBy.ID, "ru.beru.android.qa:id/paymentPeriodIcon")  # колбаска
    dateTextView = (MobileBy.ID, "ru.beru.android.qa:id/dateTextView")  # дата
    amountTextView = (MobileBy.ID, "ru.beru.android.qa:id/amountTextView")  # сумма платежа

    secondTableItem = (MobileBy.ID, "ru.beru.android.qa:id/secondTableItem")  # второй блок графика
    thirdTableItem = (MobileBy.ID, "ru.beru.android.qa:id/thirdTableItem")  # третий блок графика
    fourthTableItem = (MobileBy.ID, "ru.beru.android.qa:id/fourthTableItem")  # четвертый блок графика

    moreInfoTextView = (MobileBy.ID, "ru.beru.android.qa:id/moreInfoTextView")  # подробнее
    # moreInfoTextViewAfterOpen = (MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView")
    moreInfoTextViewAfterOpen = (
        MobileBy.XPATH, "//android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView")

    # Виджет Рассрочки
    offerInstallmentsBlock = (MobileBy.ID, "ru.beru.android.qa:id/offerInstallmentsBlock")  # виджет
    installmentsTitleTextView = (
        MobileBy.ID, "ru.beru.android.qa:id/installmentsTitleTextView")  # Рассрочка от Тинькофф
    installmentsTermView = (MobileBy.ID, "ru.beru.android.qa:id/installmentsTermView")  # блок на 3 мес = ... ₽/мес
    onePeriodTextView = (MobileBy.ID, "ru.beru.android.qa:id/onePeriodTextView")  # 3 мес
    monthlyPayment = (MobileBy.ID, "ru.beru.android.qa:id/monthlyPayment")  # ... ₽/мес
    installmentsOrderButton = (MobileBy.ID, "ru.beru.android.qa:id/installmentsOrderButton")  # Оформить
    internalNumberPicker = (MobileBy.ID, "ru.beru.android.qa:id/internalNumberPicker")  # барабан
    picker = (MobileBy.ID, "ru.beru.android.qa:id/picker")
    border = (MobileBy.ID, "ru.beru.android.qa:id/border")
    # pop-up
    slideIndicatorView = (MobileBy.ID, "ru.beru.android.qa:id/slideIndicatorView")  # слайдер
    design_bottom_sheet = (MobileBy.ID, "ru.beru.android.qa:id/design_bottom_sheet")
    bottomSheetContentContainer = (MobileBy.ID, "ru.beru.android.qa:id/bottomSheetContentContainer")
    orderId = (MobileBy.ID, "ru.beru.android.qa:id/orderId")  # Выберите срок рассрочки
    periodValuesRecyclerView = (MobileBy.ID, "ru.beru.android.qa:id/periodValuesRecyclerView")  # блок с периодами
    rootContainer1 = (MobileBy.XPATH,
                      "//android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout")  # квадратики с периодом и ценой
    rootContainer2 = (MobileBy.XPATH,
                      "//android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout")  # квадратики с периодом и ценой
    rootContainer3 = (MobileBy.XPATH,
                      "//android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.LinearLayout")  # квадратики с периодом и ценой
    rootContainer4 = (MobileBy.XPATH,
                      "//android.widget.FrameLayout[4]/android.widget.FrameLayout/android.widget.LinearLayout")  # квадратики с периодом и ценой
    periodTitle1 = (MobileBy.XPATH,
                    "//android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView[1]")  # 3 мес
    periodTitle2 = (MobileBy.XPATH,
                    "//android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView[1]")  # 3 мес
    periodTitle3 = (MobileBy.XPATH,
                    "//android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView[1]")  # 3 мес
    periodTitle4 = (MobileBy.XPATH,
                    "//android.widget.FrameLayout[4]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView[1]")  # 3 мес
    periodPrice1 = (MobileBy.XPATH,
                    "//android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView[2]")  # по 11111 ₽
    periodPrice2 = (MobileBy.XPATH,
                    "//android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView[2]")  # по 11111 ₽
    periodPrice3 = (MobileBy.XPATH,
                    "//android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView[2]")  # по 11111 ₽
    periodPrice4 = (MobileBy.XPATH,
                    "//android.widget.FrameLayout[4]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView[2]")  # по 11111 ₽
    okButton = (MobileBy.ID, "ru.beru.android.qa:id/okButton")  # Выбрать

    # Виджет Кредита
    offerCreditBlock = (MobileBy.ID, "ru.beru.android.qa:id/offerCreditBlock")  # виджет
    cartTinkoffCreditBlockTitle = (
        MobileBy.ID, "ru.beru.android.qa:id/cartTinkoffCreditBlockTitle")  # Кредит от Тинькофф
    cartTinkoffCreditBlockMonthPayment = (
        MobileBy.ID, "ru.beru.android.qa:id/cartTinkoffCreditBlockMonthPayment")  # от ... ₽ / мес.
    proceedCredit = (MobileBy.ID, "ru.beru.android.qa:id/proceed_credit")  # Оформить

    # Хэддер
    pricesContainer = (MobileBy.ID, "ru.beru.android.qa:id/pricesContainer")
    pricesBasePriceView = (MobileBy.ID, "ru.beru.android.qa:id/pricesBasePriceView")
    pricesPriceView = (MobileBy.ID, "ru.beru.android.qa:id/pricesPriceView")
    creditPriceView = (
        MobileBy.ID, "ru.beru.android.qa:id/creditPriceView")  # от ... ₽ / мес. в компактном оффере [@index = 1]
    cartCounterButton = (MobileBy.ID, "ru.beru.android.qa:id/cartCounterButton")

    def __init__(self, driver):
        super().__init__(driver)
