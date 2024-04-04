from selenium.webdriver.common.by import By


class SortablePageLocators:
    LIST_TAB = (By.CSS_SELECTOR, 'a[id="demo-tab-list"]')
    GRID_TAB = (By.CSS_SELECTOR, 'a[id="demo-tab-grid"]')
    LIST_ITEMS = (By.CSS_SELECTOR, 'div[class="list-group-item list-group-item-action"]')
    GRID_ITEMS_CONTAINER = (By.CSS_SELECTOR, 'div[id="demo-tabpane-grid"]')


class SelectablePageLocators:
    LIST_TAB = (By.CSS_SELECTOR, 'a[id="demo-tab-list"]')
    GRID_TAB = (By.CSS_SELECTOR, 'a[id="demo-tab-grid"]')
    LIST_ITEMS = (By.CSS_SELECTOR, 'li[class*="list-group-item list-group-item-action"]')
    GRID_ITEMS_CONTAINER = (By.CSS_SELECTOR, 'div[id="demo-tabpane-grid"]')
    ACTIVE_ITEMS_LIST = (By.CSS_SELECTOR, 'li[class*="list-group-item active list-group-item-action"]')

class ResizablePageLocators:
    INNER_BOX = (By.CSS_SELECTOR, 'div[id="resizableBoxWithRestriction"]')
    INNER_BOX_HANDLE = (By.CSS_SELECTOR, 'div[id="resizableBoxWithRestriction"] span')
    OUTER_BOX = (By.CSS_SELECTOR, 'div[id="resizable"]')
    OUTER_BOX_HANDLE = (By.CSS_SELECTOR, 'div[id="resizable"] span')
