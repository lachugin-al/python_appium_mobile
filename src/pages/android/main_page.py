from appium.webdriver.common.mobileby import MobileBy
from src.appium_setup import Driver


class MainPage(Driver):
    """
    главная
    """

    welcomeContent = (MobileBy.ID, 'ru.beru.android.qa:id/content')
    closeButton = (MobileBy.XPATH, '//android.widget.ImageView[@content-desc="Закрыть"]')
    sliderIndicator = (MobileBy.ID, 'ru.beru.android.qa:id/slideIndicatorView')
    cookieContainer = (MobileBy.ID, 'ru.beru.android.qa:id/rootContainer')
    negativeButton = (MobileBy.ID, 'ru.beru.android.qa:id/negativeButton')
    positiveButton = (MobileBy.ID, 'ru.beru.android.qa:id/positiveButton')
    navCatalog = (MobileBy.ID, 'ru.beru.android.qa:id/nav_catalog')
    navCart = (MobileBy.ID, 'ru.beru.android.qa:id/nav_cart')
    navProfile = (MobileBy.ID, 'ru.beru.android.qa:id/nav_profile')
    searchRequestView = (MobileBy.ID, 'ru.beru.android.qa:id/searchRequestView')

    allertTitle = (MobileBy.ID, "ru.beru.android.qa:id/alertTitle") # class android.widget.TextView[@text="Что-то пошло не так"]

    def __init__(self, driver):
        super().__init__(driver)
