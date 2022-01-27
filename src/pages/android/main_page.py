from appium.webdriver.common.mobileby import MobileBy
from src.appium_setup import Driver


class MainPage(Driver):
    """
    главная
    """

    welcomeContent = (MobileBy.ID, 'ru.beru.android.qa:id/content')
    closeButton = (MobileBy.XPATH, '//android.widget.ImageView[@content-desc="Закрыть"]')
    coupon_slider = (MobileBy.ID, 'ru.beru.android.qa:id/slideIndicatorView')


    def __init__(self, driver):
        super().__init__(driver)