import time

import pytest

from pages.widgets_page import AccordianPage, AutoCompletePage


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

