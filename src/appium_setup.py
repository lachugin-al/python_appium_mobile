from appium import webdriver
import unittest
import os
from datetime import datetime


android_desired_caps = {
            "app": "/Users/lachugin/IdeaProjects/appiumMRT/app/bluemarket-android.apk",
            "automationName": "UIAutomator2",
            "platformName": "Android",
            "platformVersion": "11.0",
            "deviceName": "Android Emulator",
            "noReset": True,
        }

ios_desired_caps = {
            "app": "",
            "automationName": "xcuitest",
            "platformName": "iOS",
            "platformVersion": "12.2",
            "deviceName": "iPhone 8 Simulator",
        }

class Driver(unittest.TestCase):

    def __init__(self, driver):
        super().__init__(driver)

    def setUp(self):
        url = "http://localhost:4723/wd/hub"
        self.driver = webdriver.Remote(url, android_desired_caps)
        self.driver.implicitly_wait(5)

    def tearDown(self):
        Driver.screenshot_on_failure(self)
        self.driver.quit()

    def screenshot_on_failure(self):
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        test_name = self._testMethodName
        for self._testMethodName, error in self._outcome.errors:
            if error:
                if not os.path.exists('screenshots'):
                    os.makedirs('screenshots')

                self.driver.save_screenshot(f"screenshots/{test_name}_{now}.png")

if __name__ == '__main__':
    unittest.main()
