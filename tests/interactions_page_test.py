import time

from pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage, DragabblePage


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

    class TestDroppablePage:
        def test_move_simple_drag_box(self, browser):
            page = DroppablePage(browser, 'https://demoqa.com/droppable')
            page.open()
            simple_drag_box = page.locators.SIMPLE_DRAG_BOX
            drop_box_text_before = page.get_text_of_visible_drop_boxes()
            assert drop_box_text_before[0] == 'Drop here', 'Text in drop box should be "Drop here"'
            page.move_drag_box_to_simple_drop_box(simple_drag_box)
            drop_box_text_after = page.get_text_of_visible_drop_boxes()
            assert drop_box_text_after[0] == 'Dropped!', 'Text in drop box should change to "Dropped!"'

        def test_move_not_acceptable_drag_box(self, browser):
            page = DroppablePage(browser, 'https://demoqa.com/droppable')
            page.open()
            page.go_to_accept_tab()
            not_acceptable_drag_box = page.locators.NOT_ACCEPTABLE_DRAG_BOX
            drop_box_text_before = page.get_text_of_visible_drop_boxes()
            assert drop_box_text_before[0] == 'Drop here', 'Text in drop box should be "Drop here"'
            page.move_drag_box_to_simple_drop_box(not_acceptable_drag_box)
            drop_box_text_after = page.get_text_of_visible_drop_boxes()
            assert drop_box_text_after[0] == 'Drop here', 'Text in drop box should be "Drop here"'

        def test_move_acceptable_drag_box(self, browser):
            page = DroppablePage(browser, 'https://demoqa.com/droppable')
            page.open()
            page.go_to_accept_tab()
            acceptable_drag_box = page.locators.ACCEPTABLE_DRAG_BOX
            drop_box_text_before = page.get_text_of_visible_drop_boxes()
            assert drop_box_text_before[0] == 'Drop here', 'Text in drop box should be "Drop here"'
            page.move_drag_box_to_simple_drop_box(acceptable_drag_box)
            drop_box_text_after = page.get_text_of_visible_drop_boxes()
            assert drop_box_text_after[0] == 'Dropped!', 'Text in drop box should change to "Dropped!"'

        def test_will_revert_drag_box(self, browser):
            page = DroppablePage(browser, 'https://demoqa.com/droppable')
            page.open()
            page.go_to_revert_draggable_tab()
            will_revert_drag_box = page.locators.WILL_REVERT_DROP_BOX
            drop_box_text_before = page.get_text_of_visible_drop_boxes()
            assert drop_box_text_before[0] == 'Drop here', 'Text in drop box should be "Drop here"'
            location_before = page.get_element_location(will_revert_drag_box)
            page.move_drag_box_to_simple_drop_box(will_revert_drag_box)
            drop_box_text_after = page.get_text_of_visible_drop_boxes()
            assert drop_box_text_after[0] == 'Dropped!', 'Text in drop box should change to "Dropped!"'
            page.element_is_stationary(will_revert_drag_box)
            location_after = page.get_element_location(will_revert_drag_box)
            assert location_before == location_after, 'Drag box is not returned after moving'

        def test_not_revert_drag_box(self, browser):
            page = DroppablePage(browser, 'https://demoqa.com/droppable')
            page.open()
            page.go_to_revert_draggable_tab()
            not_revert_drag_box = page.locators.NOT_REVERT_BOX
            drop_box_text_before = page.get_text_of_visible_drop_boxes()
            assert drop_box_text_before[0] == 'Drop here', 'Text in drop box should be "Drop here"'
            page.move_drag_box_to_simple_drop_box(not_revert_drag_box)
            location_after_move = page.get_element_location(not_revert_drag_box)
            drop_box_text_after = page.get_text_of_visible_drop_boxes()
            assert drop_box_text_after[0] == 'Dropped!', 'Text in drop box should change to "Dropped!"'
            page.element_is_stationary(not_revert_drag_box)
            finally_location = page.get_element_location(not_revert_drag_box)
            assert location_after_move == finally_location, 'Drag box is returned after moving'

        def test_outer_not_greedy_drop_box(self, browser):
            page = DroppablePage(browser, 'https://demoqa.com/droppable')
            page.open()
            page.go_to_prevent_propagation_tab()
            drag_box = page.element_is_present(page.locators.PREVENT_PROPAGATION_DRAG_BOX)
            drop_box = page.element_is_present(page.locators.INNER_DROP_BOX_NOT_GREEDY)
            visible_drop_boxes_text_before = page.get_text_of_visible_drop_boxes()
            page.drag_and_drop_to_element(drag_box, drop_box)
            visible_drop_boxes_text_after = page.get_text_of_visible_drop_boxes()
            assert visible_drop_boxes_text_before[0] == 'Outer droppable', ('Outer droppable box text is not "Outer '
                                                                            'droppable"')
            assert visible_drop_boxes_text_before[1] == 'Inner droppable (not greedy)', ('Inner droppable box text is '
                                                                                         'not "Inner droppable (not '
                                                                                         'greedy)"')
            assert visible_drop_boxes_text_after[0] == 'Dropped!', ('Outer droppable box text should change to '
                                                                    '"Dropped!"')
            assert visible_drop_boxes_text_after[1] == 'Dropped!', ('Inner droppable box text should change to '
                                                                    '"Dropped!"')

        def test_outer_greedy_drop_box(self, browser):
            page = DroppablePage(browser, 'https://demoqa.com/droppable')
            page.open()
            page.go_to_prevent_propagation_tab()
            drag_box = page.element_is_present(page.locators.PREVENT_PROPAGATION_DRAG_BOX)
            drop_box = page.element_is_present(page.locators.INNER_DROP_BOX_GREEDY)
            visible_drop_boxes_text_before = page.get_text_of_visible_drop_boxes()
            page.drag_and_drop_to_element(drag_box, drop_box)
            visible_drop_boxes_text_after = page.get_text_of_visible_drop_boxes()
            assert visible_drop_boxes_text_before[2] == 'Outer droppable', ('Outer droppable box text should be "Outer '
                                                                            'droppable"')
            assert visible_drop_boxes_text_before[3] == 'Inner droppable (greedy)', ('Inner droppable box text should '
                                                                                     'be "Inner droppable (greedy)"')
            assert visible_drop_boxes_text_after[2] == 'Outer droppable', 'Outer droppable box text should not change'
            assert visible_drop_boxes_text_after[3] == 'Dropped!', ('Inner droppable box text should change to '
                                                                    '"Dropped!"')

    class TestDragabblePage:
        def test_move_simple_drag_box(self, browser):
            page = DragabblePage(browser, 'https://demoqa.com/dragabble')
            page.open()
            drag_box = page.element_is_present(page.locators.SIMPLE_DRAG_BOX)
            drag_box_location_before = drag_box.location
            page.drag_and_drop_by_random_offset(drag_box, 1, 100)
            drag_box_location_after = drag_box.location
            assert (drag_box_location_before['x'] != drag_box_location_after['x'] and
                    drag_box_location_before['y'] != drag_box_location_after['y']), \
                'Drag box do not move correctly'

        def test_only_x_axis_drag_box(self, browser):
            page = DragabblePage(browser, 'https://demoqa.com/dragabble')
            page.open()
            page.go_to_axis_restricted_tab()
            drag_box = page.element_is_present(page.locators.ONLY_X_DRAG_BOX)
            drag_box_location_before = drag_box.location
            page.drag_and_drop_by_random_offset(drag_box, 50, 200)
            drag_box_location_after = drag_box.location
            assert drag_box_location_before['x'] != drag_box_location_after['x'], 'Drag box should moved by x axis'
            assert drag_box_location_before['y'] == drag_box_location_after['y'], 'Drag box should not moved by y axis'

        def test_only_y_axis_drag_box(self, browser):
            page = DragabblePage(browser, 'https://demoqa.com/dragabble')
            page.open()
            page.go_to_axis_restricted_tab()
            drag_box = page.element_is_present(page.locators.ONLY_Y_DRAG_BOX)
            drag_box_location_before = drag_box.location
            page.drag_and_drop_by_random_offset(drag_box, 50, 200)
            drag_box_location_after = drag_box.location
            assert drag_box_location_before['x'] == drag_box_location_after['x'], 'Drag box should not moved by x axis'
            assert drag_box_location_before['y'] != drag_box_location_after['y'], 'Drag box should moved by y axis'

        def test_drag_box_inside_the_container(self, browser):
            page = DragabblePage(browser, 'https://demoqa.com/dragabble')
            page.open()
            page.go_to_container_restricted_tab()
            drag_box = page.element_is_visible(page.locators.LARGE_CONTAINER_DRAG_BOX)
            container = page.element_is_visible(page.locators.LARGE_CONTAINER)
            check_occurrence_before = page.check_element_inside_another_element(drag_box, container)
            page.drag_and_drop_to_element(drag_box, container)
            page.drag_and_drop_by_random_offset(drag_box, 200, 300)
            check_occurrence_after = page.check_element_inside_another_element(drag_box, container)
            assert check_occurrence_before is True, 'Drag box goes outside the box'
            assert check_occurrence_after is True, 'Drag box goes outside the box'

        def test_drag_box_inside_the_parent(self, browser):
            page = DragabblePage(browser, 'https://demoqa.com/dragabble')
            page.open()
            page.go_to_container_restricted_tab()
            drag_box = page.element_is_visible(page.locators.SMALL_CONTAINER_DRAG_BOX)
            container = page.element_is_visible(page.locators.SMALL_CONTAINER)
            check_occurrence_before = page.check_element_inside_another_element(drag_box, container)
            page.drag_and_drop_by_random_offset(drag_box, 250, 300)
            check_occurrence_after = page.check_element_inside_another_element(drag_box, container)
            assert check_occurrence_before is True, 'Drag box goes outside the parent'
            assert check_occurrence_after is True, 'Drag box goes outside the parent'

            