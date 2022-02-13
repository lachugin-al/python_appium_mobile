from appium.webdriver.common.mobileby import MobileBy
from src.appium_setup import Driver


class CatalogPage(Driver):
    """
    каталог
    """

    # Строка поиска
    viewSearchAppBarLayoutContainer = (MobileBy.ID, 'ru.beru.android.qa:id/viewSearchAppBarLayoutContainer')
    viewSearchAppBarLayoutInput = (MobileBy.ID, 'ru.beru.android.qa:id/viewSearchAppBarLayoutInput')
    itemTitle = (MobileBy.ID, 'ru.beru.android.qa:id/itemTitle')

    # Оффер
    installmentGroupView = (MobileBy.ID, "ru.beru.android.qa:id/installmentGroupView")  # картинка рассрочки на фотке
    installmentTitle = (MobileBy.ID, "ru.beru.android.qa:id/installmentTitle")  # РАССРОЧКА
    installmentBody = (MobileBy.ID, "ru.beru.android.qa:id/installmentBody")  # блок с цифрами 003
    installmentFirstPeriod = (MobileBy.ID, "ru.beru.android.qa:id/installmentFirstPeriod")  # 1 цифра
    installmentSecondPeriod = (MobileBy.ID, "ru.beru.android.qa:id/installmentSecondPeriod")  # 2 цифра
    installmentThirdPeriod = (MobileBy.ID, "ru.beru.android.qa:id/installmentThirdPeriod")  # 3 цифра

    priceView = (MobileBy.ID, 'ru.beru.android.qa:id/priceView')  # цена оффера
    creditContainer = (MobileBy.ID, "ru.beru.android.qa:id/creditContainer")  # контейнер для кредита / рассрочки
    creditTitleView = (MobileBy.ID, 'ru.beru.android.qa:id/creditViewTitle')  # рассрочка
    creditViewTitle = (MobileBy.ID, "ru.beru.android.qa:id/creditViewTitle")  # можно частями / кредит
    creditViewLayout = (MobileBy.ID, "ru.beru.android.qa:id/creditViewLayout")  # блок [* ₽ / мес] для кредита / рассрочки
    creditView = (MobileBy.ID, "ru.beru.android.qa:id/creditView")  # * ₽ / мес или * ₽
    creditSmallView = (MobileBy.ID, 'ru.beru.android.qa:id/creditSmallView')  # × 3 мес

    def __init__(self, driver):
        super().__init__(driver)
