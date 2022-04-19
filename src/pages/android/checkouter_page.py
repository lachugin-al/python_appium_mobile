from appium.webdriver.common.mobileby import MobileBy
from src.appium_setup import Driver


class CheckouterPage(Driver):
    """
    Чекаутер
    """

    toolbarText = (MobileBy.XPATH,
                   "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView")

    def __init__(self, driver):
        super().__init__(driver)
