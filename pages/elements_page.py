from generator.generator import generated_person
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonLocators, \
    WebTablesLocators
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time
import random
from selenium.webdriver.support.ui import Select


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ITEMS_LIST)
        count = 21
        while count != 0:
            item = item_list[random.randint(1, 15)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    def get_checked_checkboxes(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element(*self.locators.TITLE_ITEM).text
            data.append(title_item)
        return str(data).replace(' ', '').replace('.doc', '').lower()

    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).lower().replace(' ', '')


class RadioButtonPage(BasePage):
    locators = RadioButtonLocators()

    def yes_button_click(self):
        self.element_is_clickable(self.locators.YES_RADIO_BUTTON).click()

    def no_button_click(self):
        self.element_is_clickable(self.locators.NO_RADIO_BUTTON).click()

    def impressive_button_click(self):
        self.element_is_clickable(self.locators.IMPRESSIVE_RADIO_BUTTON).click()

    def get_output_result(self):
        return self.element_is_visible(self.locators.OUTPUT_RESULT).text

    def click_on_the_radio_button(self, choice):
        choices = {
            'yes': self.locators.YES_RADIO_BUTTON,
            'impressive': self.locators.IMPRESSIVE_RADIO_BUTTON,
            'no': self.locators.NO_RADIO_BUTTON
        }
        radio = self.element_is_visible(choices[choice]).click()


class WebTablePage(BasePage):
    locators = WebTablesLocators()

    def get_row(self, num=0):
        self.row_number_assert(num)
        edit_buttons = self.elements_are_visible(self.locators.EDIT_BUTTONS)
        row = edit_buttons[num].find_element(
            *self.locators.ROW_PARENT)
        return row

    def get_row_data(self, num=0):
        self.row_number_assert(num)
        return self.get_row(num).text.splitlines()

    def get_list_of_completed_rows(self):
        return self.elements_are_visible(self.locators.EDIT_BUTTONS)

    def get_count_of_completed_rows(self):
        return len(self.elements_are_visible(self.locators.EDIT_BUTTONS))

    def get_random_row_number(self):
        return random.randint(0, (len(self.get_list_of_completed_rows()) - 1))

    def get_table_data(self):
        rows = self.get_count_of_completed_rows()
        data = []
        for row in range(rows):
            data.append(self.get_row_data(row))
        return data

    def edit_random_field_and_return_data(self):
        person_info = next(generated_person())
        person_data = [person_info.first_name,
                       person_info.last_name,
                       person_info.email,
                       str(person_info.age),
                       str(person_info.salary),
                       person_info.department]
        input_fields = self.elements_are_present(self.locators.INPUT_FIELDS)
        edit_field_choice = random.randint(0, (len(input_fields) - 1))
        input_fields[edit_field_choice].clear()
        input_fields[edit_field_choice].send_keys(person_data[edit_field_choice])
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        return person_data[edit_field_choice]

    def add_new_person(self, count=1):
        while count != 0:
            count -= 1
            person_info = next(generated_person())
            first_name = person_info.first_name
            last_name = person_info.last_name
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            self.element_is_visible(self.locators.ADD_BUTTON).click()
            self.element_is_visible(self.locators.FIRST_NAME_INPUT).send_keys(first_name)
            self.element_is_visible(self.locators.LAST_NAME_INPUT).send_keys(last_name)
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
            self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)
            self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
            return [first_name, last_name, str(age), email, str(salary), department]

    def check_new_added_person(self):
        person_list = self.elements_are_present(self.locators.FULL_PERSON_LIST)
        data = []
        for item in person_list:
            data.append(item.text.splitlines())
        return data

    def search_some_person(self, key_word):
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(key_word)

    def check_search_persons(self, key_word):
        delete_buttons = self.elements_are_present(self.locators.DELETE_BUTTONS)
        data = []
        count = 0
        for row in delete_buttons:
            count += 1
            row_data = row.find_element(*self.locators.ROW_PARENT).text.splitlines()
            assert str(key_word) in row_data, f'"{key_word}" not found in line №{count}'
        return data

    def click_on_edit_button(self, num):
        self.row_number_assert(num)
        self.get_row(num).find_element(*self.locators.EDIT_BUTTONS).click()

    def click_on_delete_button(self, num):
        self.row_number_assert(num)
        self.get_row(num).find_element(*self.locators.DELETE_BUTTONS).click()

    def row_number_assert(self, num):
        assert num >= 0, 'Row number must be positive'
        assert num < len(self.get_list_of_completed_rows()), 'This row is empty'

    def select_count_rows(self):
        select_values = [5, 10, 20, 25, 50, 100]
        data = []
        for value in select_values:
            select_button = self.element_is_visible(self.locators.SELECT_COUNT_ROWS)
            select = Select(select_button)
            select.select_by_value(f'{value}')
            data.append(self.check_count_rows())
        assert select_values == data, 'The number of rows does not match the selected value'

    def check_count_rows(self):
        return len(self.elements_are_present(self.locators.FULL_PERSON_LIST))
