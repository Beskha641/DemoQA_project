from generator.generator import generated_person
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonLocators, \
    WebTablesLocators
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time
import random


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

    def update_person_info(self):
        # generate input data
        person_info = next(generated_person())
        person_data = [person_info.first_name,
                       person_info.last_name,
                       person_info.email,
                       str(person_info.age),
                       str(person_info.salary),
                       person_info.department]

        # click the random edit button
        edit_buttons = self.elements_are_visible(self.locators.EDIT_BUTTONS)
        edit_button_choice = random.randint(0, (len(edit_buttons)-1))
        person_data_before_change = edit_buttons[edit_button_choice].find_element(*self.locators.ROW_PARENT).text.splitlines()
        edit_buttons[edit_button_choice].click()

        # choice and edit random input field
        input_fields = self.elements_are_present(self.locators.INPUT_FIELDS)
        edit_field_choice = random.randint(0, 5)
        input_fields[edit_field_choice].clear()
        input_fields[edit_field_choice].send_keys(person_data[edit_field_choice])
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        edit_buttons = self.elements_are_visible(self.locators.EDIT_BUTTONS)

        # get the data after change
        person_data_after_change = edit_buttons[edit_button_choice].find_element(*self.locators.ROW_PARENT).text.splitlines()

        # checked changed value in the row
        assert  person_data[edit_field_choice] in person_data_after_change, 'The changed value does not match the entered value'