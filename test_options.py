from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from config import URL

import pytest


# параметры Chrome
@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')
    # запуск браузера в развернутом виде
    options.add_argument('--start-maximized')

    return options


# инициализация драйвера
@pytest.fixture(autouse=True)
def testing(get_chrome_options):
    options = get_chrome_options
    selenium = webdriver.Chrome(options=options)
    selenium.implicitly_wait(10)
    selenium.get(URL)

    yield selenium
    selenium.quit()
