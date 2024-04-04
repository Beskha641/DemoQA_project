from pages.interactions_page import SortablePage


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
