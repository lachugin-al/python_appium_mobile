from appium.webdriver.common.mobileby import MobileBy
from src.appium_setup import Driver


class CartPage(Driver):
    """
    корзина
    """

    def __init__(self, driver):
        super().__init__(driver)