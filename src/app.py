from selenium.webdriver.support.wait import WebDriverWait
from src.appium_setup import Driver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import time


def keyword_check(kwargs):
    kc = {}
    if 'index' in kwargs: kc['index'] = 'elements'
    if 'index' not in kwargs: kc['index'] = 'element'
    return ''.join(kc.values())


class App(Driver):

    def __init__(self, driver):
        super().__init__(driver)
        # self.logger = None

    def element(self, locator, n=3):
        """
        элемент не найден
        """
        wait = WebDriverWait(self.driver, 20)

        x = iter(CustomCall())
        while n > 1:
            try:
                wait.until(EC.visibility_of_element_located(locator))
                return self.driver.find_element(*locator)
            except Exception as e:
                self.logger.error(f"попытка {next(x)} - {locator}")
                n -= 1
                if n == 1: raise NoSuchElementException("не найдет элемент по значению: %s" % str(locator))

    def elements(self, locator, n=3):
        """
        список элементов
        """
        wait = WebDriverWait(self.driver, 20)

        x = iter(CustomCall())
        while n > 1:
            try:
                wait.until(EC.visibility_of_any_elements_located(locator))
                return self.driver.find_elements(*locator)
            except Exception as e:
                self.logger.error(f"попытка {next(x)} - {locator}")
                n -= 1
                if n == 1: raise NoSuchElementException("не найдет элемент по значению: %s" % str(locator))

    def is_displayed(self, locator, expected=True, n=3, **kwargs):
        """
        проверяет наличие отображения элемента
        """
        wait = WebDriverWait(self.driver, 20)

        x = iter(CustomCall())
        while n > 1:
            try:
                if len(kwargs) == 0:
                    wait.until(EC.visibility_of_element_located(locator))
                    assert self.driver.find_element(*locator).is_displayed() == expected
                else:
                    assert self.driver.find_elements(*locator)[kwargs['index']].is_displayed() == expected
                break
            except Exception as e:
                self.logger.error(f'попытка {next(x)}- {locator}')
                time.sleep(0.5)
                n -= 1
                if n == 1: assert False == expected

    def is_exist(self, locator, expected=True, n=3, **kwargs):
        """
        возвращает True или False при проверке наличия элемента
        """
        while n > 1:
            try:
                if len(kwargs) == 0 and self.driver.find_element(*locator).is_displayed() == expected:
                    return True
                elif self.driver.find_elements(*locator)[kwargs['index']].is_displayed() == expected:
                    return True
            except Exception as e:
                n -= 1
                if n == 1: return False

    def click(self, locator, n=3, **kwargs):
        """
        нажать на элемент
        """
        App.sleep(kwargs)
        App.is_displayed(self, locator, True, n=n)

        return {
            'element': lambda x: App.element(self, locator).click(),
            'elements': lambda x: App.elements(self, locator)[kwargs['index']].click()
        }[keyword_check(kwargs)]('x')

    def wait_until_disappear(self, locator, n=3, **kwargs):
        wait = WebDriverWait(self.driver, 25)
        wait.until(EC.invisibility_of_element_located(locator))

    @staticmethod
    def sleep(kwargs):
        try:
            time.sleep(kwargs['sleep'])
        except KeyError:
            pass

    def send_keys(self, locator, text='', **kwargs):
        """
        напечатать сообщение
        """
        App.is_displayed(self, locator, True)

        return {
            'element': lambda text: App.element(self, locator).clear() and App.element(self, locator).send_keys(text),
            'elements': lambda text: App.elements(self, locator)[kwargs['index']].clear() and
                                     App.elements(self, locator)[kwargs['index']].send_keys(text)
        }[keyword_check(kwargs)](text)

    def get_screen_size(self):
        return self.driver.get_window_size()

    def back(self):
        """
        свернуть приложение
        """
        self.driver.back()

    def close(self):
        self.driver.close_app()

    def reset(self):
        self.driver.reset()

    def launch_app(self):
        self.driver.launch_app()

    def swipe(self, start, dest, sleep_before):
        """
        скролируем или свайпаем от одного элемента до другого
        """
        time.sleep(sleep_before)
        if type(start[1]) is not int:
            source_element = App.element(self, start)
        else:
            source_element = App.elements(self, start[0])[int(start[1])]

        if type(dest[1]) is not int:
            target_element = App.element(self, dest)
        else:
            target_element = App.elements(self, dest[0])[int(dest[1])]

        self.driver.scroll(source_element, target_element)

    def swipe_x_y(self, locator, start_x=100, start_y=200, end_x=0, end_y=0, duration=0, count=3, sleep_before=5):
        time.sleep(sleep_before)
        self.driver.implicitly_wait(1)
        for i in range(count):
            try:
                self.driver.find_element(*locator).is_displayed()
                break
            except Exception as e:
                self.driver.swipe(start_x, start_y, end_x, end_y, duration)

        self.driver.implicitly_wait(5)

    def tap(self, locator, **kwargs):
        """
        одиночное нажатие на расположение элемента
        """
        App.is_displayed(self, locator, True)

        actions = TouchAction(self.driver)
        return {
            'element': lambda x: actions.tap(App.element(self, locator)).perform(),
            'elements': lambda x: actions.tap(App.elements(self, locator)[kwargs['index']]).perform()
        }[keyword_check(kwargs)]('x')

    def double_tap(self, locator, n=3, **kwargs):
        """
        двойное нажатие на расположение элемента
        """
        App.is_displayed(self, locator, True, n=n)

        actions = TouchAction(self.driver)
        return {
            'element': lambda x: actions.tap(App.element(self, locator), count=2).perform(),
            'elements': lambda x: actions.tap(App.elements(self, locator)[kwargs['index']], count=2).perform()
        }[keyword_check(kwargs)]('x')

    def tap_x_y(self, x, y):
        time.sleep(2)
        actions = TouchAction(self.driver)
        actions.tap(x=x, y=y).perform()

    def assert_text(self, locator, text, n=20, **kwargs):
        """
        сверяет полученный текст ожидаемому значению
        """
        App.is_displayed(self, locator, True)

        x = iter(CustomCall())
        while n > 1:
            try:
                if len(kwargs) == 0:
                    assert App.element(self, locator).text.__contains__(text)
                    # assert App.element(self, locator).text == text
                else:
                    assert App.elements(self, locator)[kwargs['index']].text.__contains__(text)
                    # assert App.elements(self, locator)[kwargs['index']].text == text
                break
            except Exception as e:
                self.logger.error(f'попытка {next(x)}- {locator}')
                time.sleep(0.5)
                n -= 1
                if len(kwargs) == 0:
                    if n == 1: assert App.element(self, locator).text.__contains__(text)
                    # if n == 1: assert App.element(self, locator).text == text
                else:
                    if n == 1: assert App.elements(self, locator)[kwargs['index']].text.__contains__(text)
                    # if n == 1: assert App.elements(self, locator)[kwargs['index']].text == text

    def assert_contains_text(self, locator, text, n=20, **kwargs):
        """
        сверяет полученный текст ожидаемому значению
        """
        App.is_displayed(self, locator, True)

        x = iter(CustomCall())
        while n > 1:
            try:
                if len(kwargs) == 0:
                    assert App.element(self, locator).text.__contains__(text)
                else:
                    assert App.elements(self, locator)[kwargs['index']].text.__contains__(text)
                break
            except Exception as e:
                self.logger.error(f'попытка {next(x)}- {locator}')
                time.sleep(0.5)
                n -= 1
                if len(kwargs) == 0:
                    if n == 1: assert App.element(self, locator).text.__contains__(text)
                else:
                    if n == 1: assert App.elements(self, locator)[kwargs['index']].text.__contains__(text)

    def assert_size(self, locator, param):
        """
        сверяет размер
        """
        App.is_displayed(self, locator, True, index=0)

        case = param.rsplit(None, 1)[0]
        value = int(param.rsplit(None, 1)[1])

        if case in ['больше чем', 'выше', '>']:
            assert App.elements(self, locator).__len__() > value
        elif case in ['меньше чем', 'ниже', '<']:
            assert App.elements(self, locator).__len__() < value
        elif case in ['одинаковый', '==']:
            assert App.elements(self, locator).__len__() == value

    def assert_equal(self, actual, expected, n=5):
        x = iter(CustomCall())
        while n > 1:
            try:
                assert actual == expected
                break
            except Exception as e:
                self.logger.error(f"попытка сравнения {next(x)} - {actual} не соответствует {expected}")
                time.sleep(2)
                n -= 1
                if n == 1: assert actual == expected

    def assert_equal_ab(self, actual, expected_a, expected_b, n=5):
        x = iter(CustomCall())
        while n > 1:
            try:
                try:
                    assert actual == expected_a
                except Exception as e:
                    assert actual == expected_b
                break
            except Exception as e:
                self.logger.error(
                    f"попытка сравнения {next(x)} - {actual} не соответствует {expected_a} или {expected_b}")
                time.sleep(2)
                n -= 1
                if n == 1: assert actual == expected_a

    @staticmethod
    def assert_boolean(actual, expected=True):
        assert actual == expected


class CustomCall:

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        k = self.a
        self.a += 1
        return k
