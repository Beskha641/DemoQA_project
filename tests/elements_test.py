from pages.elements_page import TextBoxPage

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


