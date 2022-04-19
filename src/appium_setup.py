import pytest
from appium import webdriver
import unittest
import os
from datetime import datetime


class Driver(unittest.TestCase):

    def __init__(self, driver):
        super().__init__(driver)

    def setUp(self):
        """
        Метод, который инициализирует appium driver
        """
        global desired_capabilities

        if self.app == "android":
            desired_capabilities = {
                # 'app': "/Users/lachugin/code/appiumMRT/src/market_app/bluemarket-android.apk",
                'app': f'{os.popen("pwd").read().rstrip()}/src/market_app/bluemarket-android.apk',
                "automationName": "UIAutomator2",
                "platformName": "Android",
                "platformVersion": "11.0",
                "deviceName": "emulator-5554",
                "noReset": True,  # сбрасываем или нет настройки приложения при запуске (True - не сбрасываем)
            }
        elif self.app == "ios":
            desired_capabilities = {
                "app": f'{os.popen("pwd").read().rstrip()}/src/market_app/bluemarket-android.ipa',
                "automationName": "xcuitest",
                "platformName": "iOS",
                "platformVersion": "12.2",
                "deviceName": "iPhone 8 Simulator",
            }

        self.logger.info("Настройка драйвера и capabilities")
        url = "http://localhost:4723/wd/hub"
        self.driver = webdriver.Remote(url, desired_capabilities)
        self.driver.implicitly_wait(5)

    def tearDown(self):
        """
        Метод, который завершает работу appium driver
        """
        Driver.screenshot_on_failure(self)
        self.driver.quit()

    def screenshot_on_failure(self):
        """
        Метод, который делает скриншот при получении ошибки
        """
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        test_name = self._testMethodName
        for self._testMethodName, error in self._outcome.errors:
            if error:
                if not os.path.exists('screenshots'):
                    os.makedirs('screenshots')

                self.driver.save_screenshot(f"screenshots/{test_name}_{now}.png")

    @pytest.fixture(autouse=True)
    def runtime_params(self, app, logger):
        """
        Метод, который принимает параметры окружения и логгера для инициализации appium driver
        """
        self.app = app
        self.logger = logger


if __name__ == '__main__':
    unittest.main()
