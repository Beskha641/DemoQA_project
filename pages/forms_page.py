import os
import random
from selenium.webdriver import Keys

from generator.generator import generated_person, generated_file
from locators.forms_page_locators import PracticeFormPageLocators
from pages.base_page import BasePage
from selenium.webdriver.support.select import Select


class PracticeFormPage(BasePage):
    locators = PracticeFormPageLocators()

    def field_all_fields(self):
        person_info = next(generated_person())
        first_name = person_info.first_name
        last_name = person_info.last_name
        email = person_info.email
        phone_number = person_info.phone_number
        current_address = person_info.current_address
        self.element_is_visible(self.locators.FIRST_NAME_INPUT).send_keys(first_name)
        self.element_is_visible(self.locators.LAST_NAME_INPUT).send_keys(last_name)
        self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
        gender = self.click_random_radiobutton()
        self.element_is_visible(self.locators.MOBILE_INPUT).send_keys(phone_number)
        selected_date = self.select_random_date_in_calendar()
        subject = self.select_random_subject()
        checked_checkboxes = self.checked_random_checkboxes()
        file_name, path = generated_file()
        try:
            self.element_is_visible(self.locators.FILE_INPUT).send_keys(path)
        finally:
            os.remove(path)
        self.element_is_visible(self.locators.CURRENT_ADDRESS_INPUT).send_keys(current_address)
        state_and_city = self.select_state_and_city()
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        data = [f'{first_name} {last_name}', email, gender, str(phone_number), selected_date, subject,
                checked_checkboxes, path.split('\\')[-1], current_address, state_and_city]
        return data

    def click_random_radiobutton(self):
        gender = self.elements_are_visible(self.locators.GENDER_RADIO_BUTTONS)[random.randint(0, 2)]
        gender.click()
        return gender.text

    def checked_random_checkboxes(self):
        count = 7
        checkboxes = self.elements_are_visible(self.locators.HOBBIES_CHECKBOXES)
        data = []
        while count > 0:
            checked_checkbox = checkboxes[random.randint(0, 2)]
            checked_checkbox.click()
            count -= 1
            if checked_checkbox.text in data:
                data.remove(checked_checkbox.text)
            else:
                data.append(checked_checkbox.text)
        data = ', '.join(data)
        return data

    def select_random_date_in_calendar(self):
        input_field = self.element_is_visible(self.locators.DATE_OF_BIRTH_INPUT)
        input_field.click()
        selected_month = str(random.randint(0, 11))
        selected_year = str(random.randint(1900, 2100))
        Select(self.element_is_visible(self.locators.CALENDAR_MONTH)).select_by_value(selected_month)
        Select(self.element_is_visible(self.locators.CALENDAR_YEAR)).select_by_value(selected_year)
        days = self.elements_are_visible(self.locators.CALENDAR_DAYS)
        select_day = days[random.randint(0, len(days)-1)]
        selected_day = "{:02d}".format(int(select_day.text))
        selected_month_and_year = self.element_is_visible(self.locators.SELECTED_MONTH_AND_YEAR).text
        select_day.click()
        selected_date = f'{selected_day} {selected_month_and_year}'
        return selected_date

    def select_random_subject(self):
        subjects = ['Maths', 'Computer Science', 'Commerce', 'Chemistry', 'Economics', 'Physics',
                    'Biology', 'English', 'History', 'Arts']
        choice = random.choice(subjects)
        self.element_is_visible(self.locators.SUBJECTS_INPUT).send_keys(choice)
        self.element_is_visible(self.locators.SUBJECTS_INPUT).send_keys(Keys.RETURN)
        return choice

    def select_state_and_city(self):
        self.element_is_visible(self.locators.SELECT_STATE_INPUT).click()
        self.element_is_visible(self.locators.SELECT_STATE_OPTION).click()
        self.element_is_visible(self.locators.SELECT_CITY_INPUT).click()
        random.choice(self.elements_are_visible(self.locators.SELECT_CITY_OPTIONS)).click()
        address_value = self.elements_are_present(self.locators.ADDRESS_VALUES)
        return f'{address_value[0].text} {address_value[1].text}'

    def check_the_submitted_form(self):
        form_values = self.elements_are_visible(self.locators.SUBMITTED_FORM_VALUES)
        form_values_data = [element.text for element in form_values]
        form_values_data[4] = form_values_data[4].replace(',', ' ')
        return form_values_data

