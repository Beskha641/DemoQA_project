import time

from pages.interactions_page import SortablePage, SelectablePage


class TestInteractionsPage:
    class TestSortablePage:
        def test_shuffle_list_tab_items(self, browser):
            page = SortablePage(browser, 'https://demoqa.com/sortable')
            page.open()
            order_before = page.check_visible_items_order()
            page.shuffle_items()
            order_after = page.check_visible_items_order()
            assert order_before != order_after, 'Items order has not been changed'

        def test_shuffle_grid_tab_items(self, browser):
            page = SortablePage(browser, 'https://demoqa.com/sortable')
            page.open()
            page.go_to_grid_tab()
            order_before = page.check_visible_items_order()
            page.shuffle_items()
            order_after = page.check_visible_items_order()
            assert order_before != order_after, 'Items order has not been changed'

    class TestSelectablePage:
        def test_list_tab(self, browser):
            page = SelectablePage(browser, 'https://demoqa.com/selectable')
            page.open()
            clicked_items = page.click_on_random_items()
            active_items = page.check_active_items()
            assert clicked_items == active_items, 'Active items do not match clicked items'

        def test_grid_tab(self, browser):
            page = SelectablePage(browser, 'https://demoqa.com/selectable')
            page.open()
            page.go_to_grid_tab()
            clicked_items = page.click_on_random_items()
            active_items = page.check_active_items()
            assert clicked_items == active_items, 'Active items do not match clicked items'
