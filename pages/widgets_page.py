import random

from selenium.common import TimeoutException
from selenium.webdriver import Keys

from generator.generator import generated_color
from locators.widgets_page_locators import AccordianPageLocators, AutoCompletePageLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    def check_accordian(self, accordian_num):
        accordian = {
            'first': {
                'heading': self.locators.SELECTION_HEADING_FIRST,
                'content': self.locators.SELECTION_CONTENT_FIRST
            },
            'second': {
                'heading': self.locators.SELECTION_HEADING_SECOND,
                'content': self.locators.SELECTION_CONTENT_SECOND
            },
            'third': {
                'heading': self.locators.SELECTION_HEADING_THIRD,
                'content': self.locators.SELECTION_CONTENT_THIRD
            }
        }
        section_title = self.element_is_clickable(accordian[accordian_num]['heading'])
        section_title.click()
        try:
            section_content = self.element_is_visible(accordian[accordian_num]['content'])
        except TimeoutError:
            section_title.click()
            section_content = self.element_is_visible(accordian[accordian_num]['content'])

        return section_title.text, section_content.text


class AutoCompletePage(BasePage):
    locators = AutoCompletePageLocators()

    def fill_input_multi(self):
        colors = random.sample(next(generated_color()).color_name, k=random.randint(2, 11))
        input_multi = self.element_is_visible(self.locators.MULTI_INPUT)
        for color in colors:
            input_multi.send_keys(color)
            input_multi.send_keys(Keys.ENTER)
        return colors

    def check_filled_values(self, timeout=5):
        try:
            values = [value.text for value in self.elements_are_present(
                self.locators.MULTI_INPUT_VALUES, timeout=timeout)]
        except TimeoutException:
            return None
        return values

    def delete_one_of_values(self):
        values = self.elements_are_visible(self.locators.MULTI_INPUT_VALUES)
        choice_value = values[random.randint(0, (len(values) - 1))]
        deleted_value = choice_value.text
        choice_value.find_element(*self.locators.MULTI_INPUT_DELETE_BUTTONS).click()
        return deleted_value

    def delete_all_values(self):
        self.element_is_clickable(self.locators.MULTI_INPUT_DELETE_ALL_BUTTON).click()

    def fill_input_single(self):
        color = random.sample(next(generated_color()).color_name, k=1)
        input_field = self.element_is_visible(self.locators.SINGLE_INPUT)
        input_field.send_keys(color)
        input_field.send_keys(Keys.ENTER)
        return ''.join(color)

    def check_single_input_value(self):
        value = self.element_is_visible(self.locators.SINGLE_INPUT_VALUE).text
        return value
