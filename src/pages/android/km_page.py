from src.appium_setup import Driver


class KMPage(Driver):
    """
    карточка моделм/оффера
    """

    def __init__(self, driver):
        super().__init__(driver)