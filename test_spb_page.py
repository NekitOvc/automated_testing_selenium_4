'''Кейсы СПб'''

from test_options import testing, get_chrome_options
from config import URL
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import time
import requests


# TEST_001
# проверка, что пользователь может перейти на сайт
def test_open_page(testing):
    selenium = testing
    responce = requests.get(URL)

    # ожидание элемента на странице
    try:
        WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'main-nav__list')))
        print('Элемент отобразился')
    except:
        print('Элемент не отобразился')

    selenium.save_screenshot('test_open_page.png')

    assert selenium.find_element(By.CLASS_NAME, 'main-nav__list'), print('Тест провален')
    assert responce.status_code == 200, print('Тест провален')


# TEST_002
# проверка наличия в меню пиццы "Сладкая фиеста"
def test_for_kids_page_1(testing):
    selenium = testing
    # ожидание элемента на странице
    try:
        WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'main-nav__list')))
        print('Элемент отобразился')
    except:
        print('Элемент не отобразился')

    # нажать на "Да" в окне выбора города
    selenium.find_element(By.XPATH, '/html/body/div[1]/div[4]/aside/nav/div/div/div[1]/div[1]/div/div[2]/button[1]').click()

    # нажать на "Понятно" на баннере внизу сайта
    selenium.find_element(By.CLASS_NAME, 'info-button').click()
    # нажать на детское меню
    selenium.find_element(By.CLASS_NAME, 'for-kids-custom__nav').click()
    # нажать на "Показать полностью"
    selenium.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/main/div[2]/div[6]/div/div[2]/button').click()
    # нажать на поле поиска
    selenium.find_element(By.XPATH, '/html/body/div[1]/header/div[3]/div[3]/div[1]/input').click()
    time.sleep(1)
    # в поле поиска ввести "Сладкая"
    selenium.find_element(By.XPATH, '/html/body/div[1]/header/div[3]/div[3]/div[1]/input').send_keys('Сладкая')
    time.sleep(2)

    selenium.save_screenshot('test_for_kids_page_1.png')

    assert selenium.current_url == 'https://dostaevsky.ru/for-kids', print('URL не совпадает')
    assert selenium.find_element(By.CLASS_NAME, 'search-results__item-name').text == 'Пицца «Сладкая фиеста» 24 см'


# TEST_003
# проверка наличия в меню пиццы "Сырная"
def test_for_kids_page_2(testing):
    selenium = testing
    # ожидание элемента на странице
    try:
        WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'main-nav__list')))
        print('Элемент отобразился')
    except:
        print('Элемент не отобразился')

    # нажать на "Да" в окне выбора города
    selenium.find_element(By.XPATH, '/html/body/div[1]/div[4]/aside/nav/div/div/div[1]/div[1]/div/div[2]/button[1]').click()

    # нажать на "Понятно" на баннере внизу сайта
    selenium.find_element(By.CLASS_NAME, 'info-button').click()
    # нажать на детское меню
    selenium.find_element(By.CLASS_NAME, 'for-kids-custom__nav').click()
    # нажать на "Показать полностью"
    selenium.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/main/div[2]/div[6]/div/div[2]/button').click()
    # нажать на поле поиска
    selenium.find_element(By.XPATH, '/html/body/div[1]/header/div[3]/div[3]/div[1]/input').click()
    time.sleep(1)
    # в поле поиска ввести "Сырная"
    selenium.find_element(By.XPATH, '/html/body/div[1]/header/div[3]/div[3]/div[1]/input').send_keys('Сырная')
    time.sleep(2)

    selenium.save_screenshot('test_for_kids_page_2.png')

    assert selenium.current_url == 'https://dostaevsky.ru/for-kids', print('URL не совпадает')
    assert selenium.find_element(By.CLASS_NAME, 'search-results__item-name').text == 'Пицца «Сырная» 24 см'


# TEST_004
# проверка, что на странице "для детей" в описании для позиции "Сырники со сметаной и малиновым сиропом" отображается актуальные КБЖУ и вес
def test_for_kids_page_3(testing):
    selenium = testing
    # ожидание элемента на странице
    try:
        WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'main-nav__list')))
        print('Элемент отобразился')
    except:
        print('Элемент не отобразился')

    # нажать на "Да" в окне выбора города
    selenium.find_element(By.XPATH, '/html/body/div[1]/div[4]/aside/nav/div/div/div[1]/div[1]/div/div[2]/button[1]').click()

    # нажать на "Понятно" на баннере внизу сайта
    selenium.find_element(By.CLASS_NAME, 'info-button').click()
    # нажать на детское меню
    selenium.find_element(By.CLASS_NAME, 'for-kids-custom__nav').click()
    # нажать на "Показать полностью"
    selenium.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/main/div[2]/div[6]/div/div[2]/button').click()
    # нажать на поле поиска
    selenium.find_element(By.XPATH, '/html/body/div[1]/header/div[3]/div[3]/div[1]/input').click()
    time.sleep(1)
    # в поле поиска ввести "Сырники"
    selenium.find_element(By.XPATH, '/html/body/div[1]/header/div[3]/div[3]/div[1]/input').send_keys('Сырники')
    time.sleep(1)
    # нажать на позицию "Сырники"
    selenium.find_element(By.CLASS_NAME, 'search-results__item-image-name').click()
    time.sleep(1)

    selenium.save_screenshot('test_for_kids_page_3.png')

    assert selenium.current_url == 'https://dostaevsky.ru/breakfast/syrniki', print('URL не совпадает')
    assert selenium.find_element(By.TAG_NAME, 'h1').text == 'Сырники со сметаной и малиновым сиропом'
    assert selenium.find_element(By.CLASS_NAME, 'catalog-item__weight').text == '250 г'
    assert selenium.find_element(By.CLASS_NAME, 'product__energy-value').text == '615 кКал'


# TEST_005
# проверка наличия в меню позиции "Луковые кольца"
def test_vegetarian_menu_page_1(testing):
    selenium = testing
    # ожидание элемента на странице
    try:
        WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'main-nav__list')))
        print('Элемент отобразился')
    except:
        print('Элемент не отобразился')

    # нажать на "Да" в окне выбора города
    selenium.find_element(By.XPATH, '/html/body/div[1]/div[4]/aside/nav/div/div/div[1]/div[1]/div/div[2]/button[1]').click()

    # нажать на "Понятно" на баннере внизу сайта
    selenium.find_element(By.CLASS_NAME, 'info-button').click()
    # нажать на раздел для вегетарианцев
    selenium.find_element(By.CLASS_NAME, 'vegetarian-menu-custom__nav').click()
    # нажать на "Показать полностью"
    selenium.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/main/div[2]/div[6]/div/div[2]/button')
    # нажать на поле поиска
    selenium.find_element(By.XPATH, '/html/body/div[1]/header/div[3]/div[3]/div[1]/input').click()
    time.sleep(1)
    # в поле поиска ввести "Луковые"
    selenium.find_element(By.XPATH, '/html/body/div[1]/header/div[3]/div[3]/div[1]/input').send_keys('Луковые')
    time.sleep(1)

    selenium.save_screenshot('test_vegetarian_menu_page_1.png')

    assert selenium.current_url == 'https://dostaevsky.ru/vegetarian-menu'
    assert selenium.find_element(By.CLASS_NAME, 'search-results__item-name').text == 'Луковые кольца'