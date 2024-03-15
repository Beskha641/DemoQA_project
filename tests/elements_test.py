import random
import time
from selenium.webdriver.common.by import By

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage
import pytest


class TestElements:
    class TestTextBox:

        @pytest.mark.skip
        def test_text_box(self, browser):
            page = TextBoxPage(browser, 'https://demoqa.com/text-box')
            page.open()
            full_name, email, current_address, permanent_address = page.fill_all_fields()
            output_name, output_email, output_current_address, output_permanent_address = page.check_filled_form()
            assert full_name == output_name, 'The full name does not match'
            assert email == output_email, 'The email does not match'
            assert current_address == output_current_address, 'The current address does not match'
            assert permanent_address == output_permanent_address, 'The permanent address does not match'

    class TestCheckBox:
        @pytest.mark.skip
        def test_check_box(self, browser):
            page = CheckBoxPage(browser, 'https://demoqa.com/checkbox')
            page.open()
            page.open_full_list()
            page.click_random_checkbox()
            input_checkbox = page.get_checked_checkboxes()
            output_result = page.get_output_result()
            assert input_checkbox == output_result, 'Checkboxes have not been selected'

    class TestRadioButton:
        @pytest.mark.skip
        @pytest.mark.xfail('"No" have not been selected')
        def test_radio_button(self, browser):
            page = RadioButtonPage(browser, 'https://demoqa.com/radio-button')
            page.open()
            page.click_on_the_radio_button('yes')
            assert page.get_output_result() == 'Yes', 'Radio button "Yes" have not been selected'
            page.click_on_the_radio_button('impressive')
            assert page.get_output_result() == 'Impressive', 'Radio button "Impressive" have not been selected'
            page.click_on_the_radio_button('no')
            assert page.get_output_result() == 'No', 'Radio button "No" have not been selected'

    @pytest.mark.skip
    class TestWebTable:
        def test_web_table_add_person(self, browser):
            page = WebTablePage(browser, 'https://demoqa.com/webtables')
            page.open()
            new_person = page.add_new_person()
            added_person = page.check_new_added_person()
            print(new_person)
            print(added_person)
            assert new_person in added_person
            time.sleep(5)

        def test_web_table_search_person(self, browser):
            page = WebTablePage(browser, 'https://demoqa.com/webtables')
            page.open()
            key_word = page.add_new_person()[random.randint(0, 5)]
            page.search_some_person(key_word)
            page.check_search_persons(key_word)

        def test_web_table_edit_row(self, browser):
            page = WebTablePage(browser, 'https://demoqa.com/webtables')
            page.open()
            row_number = page.get_random_row_number()
            person_data_before_change = page.get_row_data(row_number)
            page.click_on_edit_button(row_number)
            new_data = page.edit_random_field_and_return_data()
            person_data_after_change = page.get_row_data(row_number)
            assert person_data_before_change != person_data_after_change, "The rows haven't changed"
            assert new_data in person_data_after_change, ('The changed value does not match the '
                                                          'entered value')

        def test_web_table_delete_rows(self, browser):
            page = WebTablePage(browser, 'https://demoqa.com/webtables')
            page.open()
            rows_before_delete = page.get_count_of_completed_rows()
            row_number = page.get_random_row_number()
            delete_row_data = page.get_row_data(row_number)
            page.click_on_delete_button(row_number)
            table_data = page.get_table_data()
            rows_after_delete = page.get_count_of_completed_rows()
            print(delete_row_data)
            print(table_data)
            assert rows_before_delete != rows_after_delete, 'The row was not deleted'
            assert delete_row_data not in table_data, 'The row remained in the table after deletion'

        def test_web_table_count_rows(self, browser):
            page = WebTablePage(browser, 'https://demoqa.com/webtables')
            select_values = [5, 10, 20, 25, 50, 100]
            page.open()
            data = page.select_count_rows()
            assert select_values == data, 'The number of rows does not match the selected value'

    class TestButtonsPage:

        def test_buttons_double_click_button(self, browser):
            page = ButtonsPage(browser, 'https://demoqa.com/buttons')
            page.open()
            page.click_on_double_click_button()
            submit_text = page.get_double_click_text()
            assert submit_text == 'You have done a double click', 'Submit text is not visible, or is incorrect'
            time.sleep(3)

        def test_buttons_right_click_button(self, browser):
            page = ButtonsPage(browser, 'https://demoqa.com/buttons')
            page.open()
            page.click_on_right_click_button()
            submit_text = page.get_right_click_text()
            assert submit_text == 'You have done a right click', 'Submit text is not visible, or is incorrect'
            time.sleep(3)

        def test_buttons_click_me_button(self, browser):
            page = ButtonsPage(browser, 'https://demoqa.com/buttons')
            page.open()
            page.click_on_click_me_button()
            submit_text = page.get_click_me_text()
            assert submit_text == 'You have done a dynamic click', 'Submit text is not visible, or is incorrect'
            time.sleep(3)
