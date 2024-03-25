from selenium.webdriver.common.by import By


class WidgetsPageLocators:
    SELECTION_HEADING_FIRST = (By.CSS_SELECTOR, 'div[id="section1Heading"]')
    SELECTION_CONTENT_FIRST = (By.CSS_SELECTOR, 'div[id="section1Content"] p')
    SELECTION_HEADING_SECOND = (By.CSS_SELECTOR, 'div[id="section2Heading"]')
    SELECTION_CONTENT_SECOND = (By.CSS_SELECTOR, 'div[id="section2Content"] p')
    SELECTION_HEADING_THIRD = (By.CSS_SELECTOR, 'div[id="section3Heading"]')
    SELECTION_CONTENT_THIRD = (By.CSS_SELECTOR, 'div[id="section3Content"] p')
