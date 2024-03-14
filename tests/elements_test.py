import random
import time
from selenium.webdriver.common.by import By

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage
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

    class TestWebTable:
        @pytest.mark.skip
        def test_web_table_add_person(self, browser):
            page = WebTablePage(browser, 'https://demoqa.com/webtables')
            page.open()
            new_person = page.add_new_person()
            added_person = page.check_new_added_person()
            print(new_person)
            print(added_person)
            assert new_person in added_person
            time.sleep(5)

        @pytest.mark.skip
        def test_web_table_search_person(self, browser):
            page = WebTablePage(browser, 'https://demoqa.com/webtables')
            page.open()
            key_word = page.add_new_person()[random.randint(0, 5)]
            page.search_some_person(key_word)
            page.check_search_persons(key_word)

        def test_edit_row(self, browser):
            page = WebTablePage(browser, 'https://demoqa.com/webtables')
            page.open()
            page = WebTablePage(browser, 'https://demoqa.com/webtables')
            page.open()
            page.update_person_info()

