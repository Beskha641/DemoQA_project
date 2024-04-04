from selenium.webdriver.common.by import By


class SortablePageLocators:
    LIST_TAB = (By.CSS_SELECTOR, 'a[id="demo-tab-list"]')
    GRID_TAB = (By.CSS_SELECTOR, 'a[id="demo-tab-grid"]')
    LIST_ITEMS = (By.CSS_SELECTOR, 'div[class="list-group-item list-group-item-action"]')
    GRID_ITEMS_CONTAINER = (By.CSS_SELECTOR, 'div[id="demo-tabpane-grid"]')
