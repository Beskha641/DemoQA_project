import allure

from pages.forms_page import PracticeFormPage
import pytest
import time

@allure.suite('Test Forms Page')
class TestFormsPage:
    @allure.feature('Test Practice Form Page')
    class TestPracticeFormPage:
        @allure.title('Test Student Registration Form')
        def test_practice_form(self, browser):
            page = PracticeFormPage(browser, 'https://demoqa.com/automation-practice-form')
            page.open()
            data_input = page.field_all_fields()
            assert (page.element_is_visible(page.locators.SUBMITTED_FORM_TITLE).text ==
                    'Thanks for submitting the form'), 'The table did not appear'
            data_output = page.check_the_submitted_form()
            assert data_input == data_output, (f'The data in the table does not match the sent data\n'
                                               f'data input: {data_input}\n'
                                               f'data output: {data_output}')
