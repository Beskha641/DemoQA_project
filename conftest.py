
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
@pytest.fixture(scope='function')
def browser():
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()
