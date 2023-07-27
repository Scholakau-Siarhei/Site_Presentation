"""All main functions are described here"""

from selenium.common import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. selenium.common.TimeoutException - исключение, которое возникает, когда таймаут истекает
# в Selenium WebDriver. Оно используется для обработки исключений при работе с WebDriver
# и ожидании элементов на странице.
# 2. selenium.webdriver.chrome.webdriver.WebDriver - класс для создания экземпляра веб-драйвера
# для браузера Google Chrome. Он используется для создания экземпляра WebDriver для автоматизации
# действий в браузере.
# 3. selenium.webdriver.support.ui.WebDriverWait - класс для ожидания элементов на странице в
# Selenium WebDriver. Он используется для задания таймаута и повторения попыток до тех пор,
# пока элемент не будет найден на странице.
# 4. selenium.webdriver.support.expected_conditions - модуль с ожидаемыми условиями в Selenium
# WebDriver. Он используется для проверки наличия определенных элементов на странице, проверки
# их видимости, доступности и других свойств.

class BasePage:
    """ Класс BasePage инициализируется с помощью WebDriver,
        который передается в конструктор как аргумент driver.
        Это означает, что каждый экземпляр класса BasePage
        будет иметь доступ к объекту WebDriver, который
        будет использоваться для поиска элементов на странице"""

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self, *args):
        """ Метод find_element() принимает два аргумента:
            by_name и by_val, которые определяют, как искать
            элемент на странице. Метод использует self.driver
            для поиска элемента на странице и возвращает найденный элемент"""
        by_name, by_val = args[0]
        return self.driver.find_element(by_name, by_val)

    def is_element_visible(self, *args):
        """ Метод is_element_visible() также принимает два аргумента:
            by_name и by_val, которые определяют, как искать элемент на странице.
            Метод использует WebDriverWait для ожидания видимости
            элемента на странице в течение 10 секунд, после чего
            он возвращает найденный элемент. Если элемент не появляется
            на странице в течение 10 секунд, возникает исключение TimeoutException"""

        by_name, by_val = args[0]
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((by_name, by_val))
        )
        return self.driver.find_element(by_name, by_val)

    def is_not_element_present(self, *args):
        """ Метод is_not_element_present() проверяет, что элемент не появляется
            на странице в течение 10 секунд. Метод принимает два аргумента:
            by_name и by_val, которые определяют, как искать элемент на странице.
            Метод использует WebDriverWait для ожидания отсутствия элемента на
            странице в течение 10 секунд. Если элемент не появляется на
            странице в течение 10 секунд, метод возвращает True. Если элемент
            все же появляется, возникает исключение TimeoutException, и метод возвращает False"""

        try:
            by_name, by_val = args[0]
            WebDriverWait(self.driver, 10).until_not(
                EC.presence_of_element_located((by_name, by_val)),
            )
        except TimeoutException:
            return False
        return True

    def is_element_present(self, *args):
        """ Метод is_element_present() проверяет, что элемент появляется
            на странице в течение 10 секунд. Метод принимает два аргумента:
            by_name и by_val, которые определяют, как искать элемент
            на странице. Метод использует WebDriverWait для ожидания
            появления элемента на странице в течение 10 секунд. Если элемент
            появляется на странице в течение 10 секунд, метод возвращает True.
            Если элемент не появляется, возникает исключение TimeoutException,
            и метод возвращает False"""

        try:
            by_name, by_val = args[0]
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((by_name, by_val)),
            )
        except TimeoutException:
            return False
        return True

    def find_elements(self, *args):
        """ Метод find_elements() находит все элементы на странице,
            соответствующие заданным параметрам поиска. Метод принимает
            два аргумента: by_name и by_val, которые определяют,
            как искать элементы на странице. Метод использует self.driver
            для поиска элементов на странице и возвращает найденные элементы"""

        by_name, by_val = args[0]
        return self.driver.find_elements(by_name, by_val)
