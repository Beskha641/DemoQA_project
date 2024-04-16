import random
import time

from selenium.webdriver.common.by import By

from locators.interactions_page_locators import SortablePageLocators, SelectablePageLocators, ResizablePageLocators, \
    DroppablePageLocators
from pages.base_page import BasePage


class SortablePage(BasePage):
    locators = SortablePageLocators()

    def get_visible_items(self):
        items = self.elements_are_present(self.locators.LIST_ITEMS)
        return [item for item in items if item.is_displayed()]

    def go_to_grid_tab(self):
        self.element_is_visible(self.locators.GRID_TAB).click()
        self.element_is_visible(self.locators.GRID_ITEMS_CONTAINER)

    def check_visible_items_order(self):
        items = self.get_visible_items()
        return [item.text for item in items]

    def shuffle_items(self):
        shuffled_count = random.randint(1, 10)
        items = self.get_visible_items()
        for i in range(shuffled_count):
            items_shuffled = random.sample(items, k=2)
            self.drag_and_drop_to_element(items_shuffled[0], items_shuffled[1])


class SelectablePage(BasePage):
    locators = SelectablePageLocators()

    def get_visible_items(self):
        items = self.elements_are_present(self.locators.LIST_ITEMS)
        return [item for item in items if item.is_displayed()]

    def go_to_grid_tab(self):
        self.element_is_visible(self.locators.GRID_TAB).click()
        self.element_is_visible(self.locators.GRID_ITEMS_CONTAINER)

    def check_active_items(self):
        active_items = self.elements_are_present(self.locators.ACTIVE_ITEMS_LIST)
        return set([item.text for item in active_items])

    def click_on_random_items(self):
        visible_items = self.get_visible_items()
        choice_items = random.sample(visible_items, k=random.randint(1, len(visible_items) - 1))
        activated_items = []
        for item in choice_items:
            activated_items.append(item.text)
            item.click()
        return set(activated_items)


class ResizablePage(BasePage):
    locators = ResizablePageLocators()

    def check_box_size(self, box):
        return box.get_attribute('style')

    def resize_box_to_min_size(self, box):
        box_handle = box.find_element(By.CSS_SELECTOR, 'span')
        self.drag_and_drop_by_offset(box_handle, -200, -200)

    def resize_box_to_max_size(self, box):
        box_handle = box.find_element(By.CSS_SELECTOR, 'span')
        self.drag_and_drop_by_offset(box_handle, 500, 300)


class DroppablePage(BasePage):
    locators = DroppablePageLocators()

    def get_visible_drop_boxes(self):
        items = self.elements_are_present(self.locators.DROP_BOXES_LIST)
        return [item for item in items if item.is_displayed()]

    def get_text_of_visible_drop_boxes(self):
        visible_drop_boxes = self.get_visible_drop_boxes()
        data = []
        for drop_box in visible_drop_boxes:
            data.append(drop_box.find_element(By.CSS_SELECTOR, 'p').text)
        return data

    def get_element_location(self, element_locator):
        return self.element_is_present(element_locator).location


    def move_drag_box_to_simple_drop_box(self, drag_box_locator):
        drop_box = self.get_visible_drop_boxes()[0]
        self.drag_and_drop_to_element(self.element_is_visible(drag_box_locator), drop_box)

    def go_to_accept_tab(self):
        self.element_is_visible(self.locators.ACCEPT_TAB).click()
        self.element_is_visible(self.locators.NOT_ACCEPTABLE_DRAG_BOX)

    def go_to_prevent_propagation_tab(self):
        self.element_is_visible(self.locators.PREVENT_PROPAGATION_TAB).click()
        self.element_is_visible(self.locators.OUTER_DROP_BOX_GREEDY)

    def go_to_revert_draggable_tab(self):
        self.element_is_visible(self.locators.REVERT_DRAGGABLE_TAB).click()
        self.element_is_visible(self.locators.WILL_REVERT_DROP_BOX)


