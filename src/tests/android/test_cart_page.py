import time

from src.app import App
from src.tests.android.test_main_page import TestMainPage
from src.pages.android.main_page import MainPage
from src.pages.android.km_page import KMPage
from src.pages.android.cart_page import CartPage


class TestCartPage(TestMainPage):

    def __init__(self, driver):
        super().__init__(driver)

    def test_3_vijets_in_cart(self):
        """Проверка наличия и отображения 3х виджетов в корзине"""

        # self.test_close_all_welcome_contents()
        self.driver.execute_script("mobile: deepLink", {
            "url": "yamarket://product--cinetic-big-ball-animal-pro-2/515571001?sku=100868870241&offerid=3G7T1VT2MrMs6k59eZdmoQ",
            "package": "ru.beru.android.qa"})
        time.sleep(10)
        App.swipe_x_y(self, locator='', start_x=500, start_y=700, count=2)
        flag = True # "1 товар в корзине"
        while flag:
            flag = App.assert_text(self, KMPage.cartButtonProgressButton, "Добавить в корзину")
            if flag:
                App.click(self, KMPage.productMainCartButton)
                flag = False
            else:
                App.click(self, KMPage.cartMinusButton)
        App.click(self, MainPage.navCart)