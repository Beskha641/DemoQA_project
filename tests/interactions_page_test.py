import time

from pages.interactions_page import SortablePage, SelectablePage, ResizablePage


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

    class TestResizablePage:

        def test_resize_inner_box(self, browser):
            page = ResizablePage(browser, 'https://demoqa.com/resizable')
            page.open()
            box = page.element_is_visible(page.locators.INNER_BOX)
            start_box_size = page.check_box_size(box)
            assert start_box_size == 'width: 200px; height: 200px;', 'Initial window size is not 200x200px'
            page.resize_box_to_min_size(box)
            min_box_size = page.check_box_size(box)
            page.resize_box_to_max_size(box)
            max_box_size = page.check_box_size(box)
            assert min_box_size == 'width: 150px; height: 150px;', 'Minimum window size is not 150x150px'
            assert max_box_size == 'width: 500px; height: 300px;', 'Maximum window size is not 500x300px'

        def test_resize_outer_box(self, browser):
            page = ResizablePage(browser, 'https://demoqa.com/resizable')
            page.open()
            box = page.element_is_visible(page.locators.OUTER_BOX)
            start_box_size = page.check_box_size(box)
            assert start_box_size == 'width: 200px; height: 200px;', 'Initial window size is not 200x200px'
            page.resize_box_to_min_size(box)
            min_box_size = page.check_box_size(box)
            page.resize_box_to_max_size(box)
            max_box_size = page.check_box_size(box)
            assert min_box_size == 'width: 20px; height: 20px;', 'Minimum window size is not 20x20px'
            assert max_box_size == 'width: 520px; height: 320px;', 'The window is not resized correctly'


