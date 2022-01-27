from appium.webdriver.common.mobileby import MobileBy
from src.appium_setup import Driver


class CatalogPage(Driver):
    """
    каталог
    """

    def __init__(self, driver):
        super().__init__(driver)