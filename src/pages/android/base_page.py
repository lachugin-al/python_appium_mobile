from src.appium_setup import Driver


class BasePage(Driver):
    """
    Базовая страница
    """

    def __init__(self, driver):
        super().__init__(driver)
