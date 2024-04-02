import random
import time

import pytest

from pages.widgets_page import AccordianPage, AutoCompletePage, DatePickerPage, SliderPage, ProgressBarPage, TabsPage, \
    ToolTipsPage, MenuPage, SelectMenuPage


class TestWidgetsPage:
    class TestAccordianPage:

        def test_accordian(self, browser):
            page = AccordianPage(browser, 'https://demoqa.com/accordian')
            page.open()
            first_section_title, first_section_content = page.check_accordian('first')
            second_section_title, second_section_content = page.check_accordian('second')
            third_section_title, third_section_content = page.check_accordian('third')
            assert first_section_title == 'What is Lorem Ipsum?' and len(first_section_content) > 0
            assert second_section_title == 'Where does it come from?' and len(second_section_content) > 0
            assert third_section_title == 'Why do we use it?' and len(third_section_content) > 0

    class TestAutoCompletePage:

        def test_multi_input(self, browser):
            page = AutoCompletePage(browser, 'https://demoqa.com/auto-complete')
            page.open()
            sent_values = page.fill_input_multi()
            actual_values = page.check_filled_values()
            assert sent_values == actual_values, 'Sent values do not match actual values'

        def test_delete_one_of_value_of_multi_input(self, browser):
            page = AutoCompletePage(browser, 'https://demoqa.com/auto-complete')
            page.open()
            filled_values_before = page.fill_input_multi()
            deleted_value = page.delete_one_of_values()
            filled_values_after = page.check_filled_values()
            assert len(filled_values_before) - 1 == len(filled_values_after), "Value don't deleted"
            assert deleted_value not in filled_values_after, 'The wrong value has been deleted'

        def test_delete_all_button(self, browser):
            page = AutoCompletePage(browser, 'https://demoqa.com/auto-complete')
            page.open()
            filled_values_before = page.fill_input_multi()
            assert len(filled_values_before) > 0, 'Input field do not filled'
            page.delete_all_values()
            filled_values_after = page.check_filled_values(1)
            assert filled_values_after is None, 'Input field is not empty'

        def test_single_input(self, browser):
            page = AutoCompletePage(browser, 'https://demoqa.com/auto-complete')
            page.open()
            sent_value = page.fill_input_single()
            checked_value = page.check_single_input_value()
            assert sent_value == checked_value, 'The sent value do not match filled value'

    class TestDatePickerPage:
        def test_select_date_input(self, browser):
            page = DatePickerPage(browser, 'https://demoqa.com/date-picker')
            page.open()
            selected_date = page.select_random_date_in_date_picker()
            date_in_date_picker = page.check_date_in_date_picker()
            assert selected_date == date_in_date_picker, 'Date do not changed'

        def test_date_and_time_picker(self, browser):
            page = DatePickerPage(browser, 'https://demoqa.com/date-picker')
            page.open()
            input_date = page.select_random_date_and_time()
            check_date = page.check_date_and_time()
            assert input_date == check_date, 'Date do not changed'

    class TestSliderPage:
        def test_slider(self, browser):
            page = SliderPage(browser, 'https://demoqa.com/slider')
            page.open()
            value_before = page.check_slider_value()
            page.drag_and_drop_slider()
            value_after = page.check_slider_value()
            assert value_after != value_before, 'The slider has not been moved'

    class TestProgressBarPage:
        def test_progress_bar(self, browser):
            page = ProgressBarPage(browser, 'https://demoqa.com/progress-bar')
            page.open()
            value_before = page.check_progress_bar_value()
            page.click_on_progress_bar_button()
            time.sleep(random.randint(1, 5))
            page.click_on_progress_bar_button()
            value_after = page.check_progress_bar_value()
            assert value_before < value_after, 'Progress bar has not moved'

    class TestTabsPage:
        @pytest.mark.xfail(reason="'More' tab is not clicable")
        def test_tabs(self, browser):
            page = TabsPage(browser, 'https://demoqa.com/tabs')
            page.open()
            page.click_on_tab(page.locators.WHAT_TAB)
            what_tab_text = page.check_text_visibility(page.locators.WHAT_TAB_TEXT)
            page.click_on_tab(page.locators.ORIGIN_TAB)
            origin_tab_text = page.check_text_visibility(page.locators.ORIGIN_TAB_TEXT)
            page.click_on_tab(page.locators.USE_TAB)
            use_tab_text = page.check_text_visibility(page.locators.USE_TAB_TEXT)
            page.click_on_tab(page.locators.MORE_TAB)
            more_tab_text = page.check_text_visibility(page.locators.MORE_TAB_TEXT)
            assert len(what_tab_text) > 0
            assert len(origin_tab_text) > 0
            assert len(use_tab_text) > 0
            assert len(more_tab_text) > 0

    class TestToolTipsPage:
        def test_hover_messages(self, browser):
            page = ToolTipsPage(browser, 'https://demoqa.com/tool-tips')
            page.open()
            (hover_button, hover_input_field, first_hover_text,
             second_hover_text) = page.get_elements_with_hover_message()
            page.move_mouse_to_element(hover_button)
            button_message = page.check_pop_up_message()
            assert button_message == 'You hovered over the Button', 'Hover message do not displayed'
            page.move_mouse_to_element(hover_input_field)
            input_field_message = page.check_pop_up_message()
            assert input_field_message == 'You hovered over the text field', 'Hover message do not displayed'
            page.move_mouse_to_element(first_hover_text)
            first_text_message = page.check_pop_up_message()
            assert first_text_message == 'You hovered over the Contrary', 'Hover message do not displayed'
            page.move_mouse_to_element(second_hover_text)
            second_text_message = page.check_pop_up_message()
            assert second_text_message == 'You hovered over the 1.10.32', 'Hover message do not displayed'

    class TestMenuPage:
        def test_sub_items(self, browser):
            page = MenuPage(browser, 'https://demoqa.com/menu#')
            page.open()
            main_item_two_menu = page.check_visibility_of_element_by_text('Main Item 2')
            page.move_mouse_to_element(main_item_two_menu)
            sub_items_list_menu = page.check_visibility_of_element_by_text('SUB SUB LIST »')
            page.move_mouse_to_element(sub_items_list_menu)
            sub_sub_item_one = page.check_visibility_of_element_by_text('Sub Sub Item 1')
            sub_sub_item_two = page.check_visibility_of_element_by_text('Sub Sub Item 2')
            assert sub_sub_item_one.text == 'Sub Sub Item 1'
            assert sub_sub_item_two.text == 'Sub Sub Item 2'

    class TestSelectMenuPage:
        def test_select_value_field(self, browser):
            page = SelectMenuPage(browser, 'https://demoqa.com/select-menu')
            page.open()
            selected_value = page.field_react_select()[-1]
            displayed_value = page.check_select_value_field()
            assert selected_value == displayed_value, 'The selected value does not match the displayed value'

        def test_one_value_field(self, browser):
            page = SelectMenuPage(browser, 'https://demoqa.com/select-menu')
            page.open()
            selected_value = page.field_react_select(1)[-1]
            displayed_value = page.check_select_one_field()
            assert selected_value == displayed_value, 'The selected value does not match the displayed value'

        def test_old_style_select_menu(self, browser):
            page = SelectMenuPage(browser, 'https://demoqa.com/select-menu')
            page.open()
            selected_value, displayed_value = page.select_value_of_old_style_select_menu()
            assert selected_value == displayed_value, 'The selected value is not displayed correctly'

        def test_multi_select_drop_down(self, browser):
            page = SelectMenuPage(browser, 'https://demoqa.com/select-menu')
            page.open()
            selected_values = page.field_react_select(2)
            displayed_values = page.check_multi_select_drop_down_values()
            assert selected_values == displayed_values, 'The selected value does not match the displayed value'

        def test_standard_multi_select(self, browser):
            page = SelectMenuPage(browser, 'https://demoqa.com/select-menu')
            page.open()
            value_colors_before, value_colors_after = page.check_standard_multi_select()
            assert value_colors_before.keys() == value_colors_after.keys(), ('The colored values do not match the '
                                                                             'selected values')
            assert value_colors_before != value_colors_after, 'Values have not been marked selected'
