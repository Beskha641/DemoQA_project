import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()


@pytest.fixture(scope='function')
def browser():
    with allure.step('Start browser'):
        options.page_load_strategy = 'eager'
        browser = webdriver.Chrome(options=options)
        yield browser
    with allure.step('Quit browser'):
        browser.quit()
