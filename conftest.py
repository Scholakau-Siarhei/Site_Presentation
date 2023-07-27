import pytest, requests, logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope='function')
def driver():
    """ Фикстура driver() создает экземпляр объекта WebDriver
        и устанавливает его настройки. Фикстура устанавливает режим
        без графического интерфейса (--headless) и отключает использование
        GPU (--disable-gpu). Фикстура также устанавливает низкий уровень
        журналирования (--log-level=3) и исключает журналирование
        (--excludeSwitches) от ChromeDriver. Затем фикстура создает
        экземпляр объекта WebDriver с помощью ChromeDriverManager и
        максимизирует окно браузера. Фикстура также устанавливает время
        неявного ожидания на 10 секунд. После прохождения всех тестов
        фикстура закрывает браузер"""

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument('log-level=3')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.accept_untrusted_certs = True
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
