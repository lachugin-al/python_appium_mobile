from src.appium_setup import Driver


class BasePage(Driver):
    """
    базовая страница
    """

    def __init__(self, driver):
        super().__init__(driver)