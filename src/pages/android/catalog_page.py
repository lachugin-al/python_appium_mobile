from appium.webdriver.common.mobileby import MobileBy
from src.appium_setup import Driver


class CatalogPage(Driver):
    """
    каталог
    """
    viewSearchAppBarLayoutContainer = (MobileBy.ID, 'ru.beru.android.qa:id/viewSearchAppBarLayoutContainer')
    viewSearchAppBarLayoutInput = (MobileBy.ID, 'ru.beru.android.qa:id/viewSearchAppBarLayoutInput')
    itemTitle = (MobileBy.ID, 'ru.beru.android.qa:id/itemTitle')

    priceView = (MobileBy.ID, 'ru.beru.android.qa:id/priceView')
    creditTitleView = (MobileBy.ID, 'ru.beru.android.qa:id/creditViewTitle')
    creditView = (MobileBy.ID, 'ru.beru.android.qa:id/creditView')
    creditSmallView = (MobileBy.ID, 'ru.beru.android.qa:id/creditSmallView')

    def __init__(self, driver):
        super().__init__(driver)