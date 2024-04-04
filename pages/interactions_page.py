import random

from locators.interactions_page_locators import SortablePageLocators, SelectablePageLocators
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



