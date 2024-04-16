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


class DroppablePageLocators:
    SIMPLE_DRAG_BOX = (By.CSS_SELECTOR, 'div[id="draggable"]')
    DROP_BOXES_LIST = (By.CSS_SELECTOR, 'div[class*="ui-droppable"]')
    ACCEPTABLE_DRAG_BOX = (By.CSS_SELECTOR, 'div[id="acceptable"]')
    NOT_ACCEPTABLE_DRAG_BOX = (By.CSS_SELECTOR, 'div[id="notAcceptable"]')
    PREVENT_PROPAGATION_DRAG_BOX = (By.CSS_SELECTOR, 'div[id="dragBox"]')
    OUTER_DROP_BOX_NOT_GREEDY = (By.CSS_SELECTOR, 'div[id="notGreedyDropBox"]')
    OUTER_DROP_BOX_NOT_GREEDY_TEXT = (By.CSS_SELECTOR, 'div[id="notGreedyDropBox"]>p')
    INNER_DROP_BOX_NOT_GREEDY = (By.CSS_SELECTOR, 'div[id="notGreedyInnerDropBox"]')
    INNER_DROP_BOX_NOT_GREEDY_TEXT = (By.CSS_SELECTOR, 'div[id="notGreedyInnerDropBox"]>p')
    OUTER_DROP_BOX_GREEDY = (By.CSS_SELECTOR, 'div[id="greedyDropBox"]')
    OUTER_DROP_BOX_GREEDY_TEXT = (By.CSS_SELECTOR, 'div[id="greedyDropBox"]>p')
    INNER_DROP_BOX_GREEDY = (By.CSS_SELECTOR, 'div[id="greedyDropBoxInner"]')
    INNER_DROP_BOX_GREEDY_TEXT = (By.CSS_SELECTOR, 'div[id="greedyDropBoxInner"]>p')
    WILL_REVERT_DROP_BOX = (By.CSS_SELECTOR, 'div[id="revertable"]')
    NOT_REVERT_BOX = (By.CSS_SELECTOR, 'div[id="notRevertable"]')

    # Tabs
    ACCEPT_TAB = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-accept"]')
    PREVENT_PROPAGATION_TAB = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-preventPropogation"]')
    REVERT_DRAGGABLE_TAB = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-revertable"]')
