import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()

@pytest.fixture(scope='function')
def browser():
    options.page_load_strategy = 'eager'
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()
