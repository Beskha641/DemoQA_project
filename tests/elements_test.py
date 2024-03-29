import random
import time

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinkPage, \
    BrokenLinksAndImagesPage, UploadAndDownloadPage, DynamicPropertiesPage
import pytest


class TestElements:
    class TestTextBox:

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

        def test_check_box(self, browser):
            page = CheckBoxPage(browser, 'https://demoqa.com/checkbox')
            page.open()
            page.open_full_list()
            page.click_random_checkbox()
            input_checkbox = page.get_checked_checkboxes()
            output_result = page.get_output_result()
            assert input_checkbox == output_result, 'Checkboxes have not been selected'

    class TestRadioButton:

        @pytest.mark.xfail(reason='"No" have not been selected')
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
        def test_web_table_add_person(self, browser):
            page = WebTablePage(browser, 'https://demoqa.com/webtables')
            page.open()
            new_person = page.add_new_person()
            added_person = page.check_new_added_person()
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

        def test_buttons_right_click_button(self, browser):
            page = ButtonsPage(browser, 'https://demoqa.com/buttons')
            page.open()
            page.click_on_right_click_button()
            submit_text = page.get_right_click_text()
            assert submit_text == 'You have done a right click', 'Submit text is not visible, or is incorrect'

        def test_buttons_click_me_button(self, browser):
            page = ButtonsPage(browser, 'https://demoqa.com/buttons')
            page.open()
            page.click_on_click_me_button()
            submit_text = page.get_click_me_text()
            assert submit_text == 'You have done a dynamic click', 'Submit text is not visible, or is incorrect'

    class TestLinkPage:

        def test_link_home(self, browser):
            page = LinkPage(browser, 'https://demoqa.com/links')
            page.open()
            home_link = page.locators.LINK_HOME
            page_url = page.go_to_link(home_link)
            assert page_url == 'https://demoqa.com/', 'Incorrect link'

        def test_dynamic_link(self, browser):
            page = LinkPage(browser, 'https://demoqa.com/links')
            page.open()
            link = page.locators.LINK_DYNAMIC
            page_url = page.go_to_link(link)
            assert page_url == 'https://demoqa.com/', 'Incorrect link'

        def test_created_link(self, browser):
            page = LinkPage(browser, 'https://demoqa.com/links')
            page.open()
            link = page.locators.LINK_CREATE
            code = page.check_link(link, 'https://demoqa.com/created')
            assert code == 201, 'Status code should be 201'

        def test_no_content_link(self, browser):
            page = LinkPage(browser, 'https://demoqa.com/links')
            page.open()
            link = page.locators.LINK_NO_CONTENT
            code = page.check_link(link, 'https://demoqa.com/no-content')
            assert code == 204, 'Status code should be 204'

        def test_moved_link(self, browser):
            page = LinkPage(browser, 'https://demoqa.com/links')
            page.open()
            link = page.locators.LINK_MOVED
            code = page.check_link(link, 'https://demoqa.com/moved')
            assert code == 301, 'Status code should be 301'

        def test_bad_request_link(self, browser):
            page = LinkPage(browser, 'https://demoqa.com/links')
            page.open()
            link = page.locators.LINK_BAD_REQUEST
            code = page.check_link(link, 'https://demoqa.com/bad-request')
            assert code == 400, 'Status code should be 400'

        def test_unauthorized_link(self, browser):
            page = LinkPage(browser, 'https://demoqa.com/links')
            page.open()
            link = page.locators.LINK_UNAUTHORIZED
            code = page.check_link(link, 'https://demoqa.com/unauthorized')
            assert code == 401, 'Status code should be 401'

        def test_forbidden_link(self, browser):
            page = LinkPage(browser, 'https://demoqa.com/links')
            page.open()
            link = page.locators.LINK_FORBIDDEN
            code = page.check_link(link, 'https://demoqa.com/forbidden')
            assert code == 403, 'Status code should be 403'

        def test_not_found_link(self, browser):
            page = LinkPage(browser, 'https://demoqa.com/links')
            page.open()
            link = page.locators.LINK_NOT_FOUND
            code = page.check_link(link, 'https://demoqa.com/invalid-url')
            assert code == 404, 'Status code should be 404'

    class TestBrokenLinksAndImagesPage:

        def test_valid_image(self, browser):
            page = BrokenLinksAndImagesPage(browser, 'https://demoqa.com/broken')
            page.open()
            img = page.locators.VALID_IMAGE
            height, width = page.check_element_size(img)
            assert height == 100 and width == 347, 'The image is not displayed correctly'

        @pytest.mark.xfail(reason='Image is not displayed')
        def test_broken_image(self, browser):
            page = BrokenLinksAndImagesPage(browser, 'https://demoqa.com/broken')
            page.open()
            img = page.locators.BROKEN_IMAGE
            height, width = page.check_element_size(img)
            assert height == 100 and width == 347, 'The image is not displayed correctly'

        @pytest.mark.xfail(reason="The link has http protocol, not https, I think this is a bug")
        def test_valid_link(self, browser):
            page = BrokenLinksAndImagesPage(browser, 'https://demoqa.com/broken')
            page.open()
            link = page.locators.VALID_LINK
            page_url = page.get_link_url(link)
            new_url = page.check_link(link, page_url)
            assert page_url == new_url, 'Incorrect link'

        def test_broken_link(self, browser):
            page = BrokenLinksAndImagesPage(browser, 'https://demoqa.com/broken')
            page.open()
            link = page.locators.BROKEN_LINK
            url = page.get_link_url(link)
            code = page.check_link(link, url)
            assert code == 500, 'Link response should be 500'

    class TestUploadAndDownloadPage:

        def test_upload_button(self, browser):
            page = UploadAndDownloadPage(browser, 'https://demoqa.com/upload-download')
            page.open()
            file_name, upload_message = page.upload_file()
            assert file_name == upload_message, 'Upload message and file name does not match'

        def test_download_button(self, browser):
            page = UploadAndDownloadPage(browser, 'https://demoqa.com/upload-download')
            page.open()
            check_file = page.download_file()
            assert check_file is True, 'The file has not been downloaded'

    class TestDynamicPropertiesPage:
        def test_text_with_random_id(self, browser):
            page = DynamicPropertiesPage(browser, 'https://demoqa.com/dynamic-properties')
            page.open()
            text = page.get_text_with_random_id()
            assert text == 'This text has random Id', 'Text not found'

        def test_appear_button(self, browser):
            page = DynamicPropertiesPage(browser, 'https://demoqa.com/dynamic-properties')
            page.open()
            result = page.check_appear_button()
            assert result is True, "The button didn't appear within 5 seconds"

        def test_enable_button(self, browser):
            page = DynamicPropertiesPage(browser, 'https://demoqa.com/dynamic-properties')
            page.open()
            result = page.check_enable_button()
            assert result is True, "The button didn't enable within 5 seconds"

        def test_color_change_button(self, browser):
            page = DynamicPropertiesPage(browser, 'https://demoqa.com/dynamic-properties')
            page.open()
            color_before, color_after = page.check_color_change_button()
            assert color_before != color_after, 'Button color has not changed within 5 seconds'
