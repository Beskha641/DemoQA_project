import random
from selenium.webdriver.common.by import By
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from generator.generator import generated_color
from locators.widgets_page_locators import AccordianPageLocators, AutoCompletePageLocators, DatePickerPageLocators, \
    SliderPageLocators, ProgressBarPageLocators, TabsPageLocators, ToolTipsPageLocators, MenuPageLocators, \
    SelectMenuPageLocators
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


class DatePickerPage(BasePage):
    locators = DatePickerPageLocators()

    def select_random_date_in_date_picker(self):
        self.element_is_visible(self.locators.DATE_SELECT).click()
        selected_month = random.randint(0, 11)
        Select(self.element_is_visible(self.locators.DATE_SELECT_MONTH)).select_by_value(str(selected_month))
        selected_year = random.randint(1900, 2100)
        Select(self.element_is_visible(self.locators.DATE_SELECT_YEAR)).select_by_value(str(selected_year))
        days = self.elements_are_present(self.locators.DATE_SELECT_DAYS_LIST)
        selected_day = random.randint(0, len(days))
        days[selected_day].click()
        return [str("{:02d}".format(selected_month + 1)), str("{:02d}".format(selected_day + 1)), str(selected_year)]

    def check_date_in_date_picker(self):
        date = self.element_is_present(self.locators.DATE_SELECT).get_attribute('value')
        return date.split('/')

    def select_random_date_and_time(self):
        self.element_is_visible(self.locators.DATE_AND_TIME_SELECT).click()
        self.element_is_visible(self.locators.DATE_AND_TIME_SELECT_MONTH).click()
        months = self.elements_are_visible(self.locators.DATE_AND_TIME_SELECT_MONTH_LIST)
        select_month = random.choice(months)
        selected_month = select_month.text
        select_month.click()
        self.element_is_visible(self.locators.DATE_AND_TIME_SELECT_YEAR).click()
        years = self.elements_are_visible(self.locators.DATE_AND_TIME_SELECT_YEAR_LIST)
        select_year = years[random.randint(1, 11)]
        selected_year = select_year.text
        select_year.click()
        days = self.elements_are_present(self.locators.DATE_SELECT_DAYS_LIST)
        select_day = random.choice(days)
        selected_day = select_day.text
        select_day.click()
        time_list = self.elements_are_present(self.locators.DATE_AND_TIME_SELECT_TIME_LIST)
        select_time = random.choice(time_list)
        selected_time = select_time.text
        formatted_time = self.time_format_to_am_pm(selected_time)
        select_time.click()
        return f'{selected_month} {selected_day}, {selected_year} {formatted_time}'

    def check_date_and_time(self):
        return self.element_is_visible(self.locators.DATE_AND_TIME_SELECT).get_attribute('value')


class SliderPage(BasePage):
    locators = SliderPageLocators()

    def drag_and_drop_slider(self):
        slider_bar = self.element_is_visible(self.locators.SLIDER_BAR)
        self.drag_and_drop_by_offset(slider_bar, random.randint(-10, 10))

    def check_slider_value(self):
        return self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')


class ProgressBarPage(BasePage):
    locators = ProgressBarPageLocators()

    def click_on_progress_bar_button(self):
        self.element_is_clickable(self.locators.PROGRESS_BAR_BUTTON).click()

    def check_progress_bar_value(self):
        return self.element_is_present(self.locators.PROGRESS_BAR).get_attribute('aria-valuenow')


class TabsPage(BasePage):
    locators = TabsPageLocators()

    def click_on_tab(self, locator):
        self.element_is_clickable(locator).click()

    def check_text_visibility(self, locator):
        return self.element_is_visible(locator).text


class ToolTipsPage(BasePage):
    locators = ToolTipsPageLocators()

    def check_pop_up_message(self):
        return self.elements_are_visible(self.locators.POP_UP_MESSAGE)[-1].text

    def get_elements_with_hover_message(self):
        button = self.element_is_visible(self.locators.BUTTON)
        input_field = self.element_is_visible(self.locators.INPUT_FIELD)
        text_elements_list = self.elements_are_visible(self.locators.HOVER_TEXT_LIST)
        return button, input_field, text_elements_list[0], text_elements_list[1]


class MenuPage(BasePage):
    locators = MenuPageLocators()

    def check_visibility_of_element_by_text(self, text):
        return self.element_is_visible((By.LINK_TEXT, f'{text}'))


class SelectMenuPage(BasePage):
    locators = SelectMenuPageLocators()

    def check_select_value_field(self):
        return self.element_is_visible(self.locators.SELECT_VALUE_FIELD_SELECTED_VALUE).text

    def check_select_one_field(self):
        return self.element_is_visible(self.locators.SELECT_ONE_FIELD_SELECTED_VALUE).text

    def select_value_of_old_style_select_menu(self):
        field = self.element_is_visible(self.locators.OLD_STYLE_SELECT_MENU)
        select = Select(field)
        data = ['Red', 'Blue', 'Green', 'Yellow', 'Purple', 'Black', 'White', 'Voilet', 'Indigo', 'Magenta', 'Aqua']
        selected_value = random.choice(data)
        select.select_by_visible_text(selected_value)
        displayed_value = select.first_selected_option.text
        return selected_value, displayed_value

    def field_multi_select_drop_down(self):
        self.element_is_visible(self.locators.MULTI_SELECT_DROP_DOWN_FIELD).click()
        sent_elements_count = random.randint(2, 4)
        print(sent_elements_count)
        sent_elements = []
        for i in range(sent_elements_count):
            element = random.choice(self.elements_are_visible(self.locators.MULTI_SELECT_DROP_DOWN_FIELD_OPTIONS))
            sent_elements.append(element.text)
            element.click()
        print(sent_elements)

    def field_react_select(self, select_index=0, options_count=random.randint(1, 4)):
        react_select_field = self.elements_are_visible(self.locators.REACT_SELECT_FIELD_LIST)[select_index]
        selected_options_list = []
        react_select_field.click()
        for option_count in range(options_count):
            try:
                options = self.elements_are_visible(self.locators.REACT_SELECT_OPTIONS, 0)
            except TimeoutException:
                react_select_field.click()
                options = self.elements_are_visible(self.locators.REACT_SELECT_OPTIONS)
            selected_option = options[random.randint(0, len(options) - 1)]
            selected_options_list.append(selected_option.text)
            selected_option.click()
        return selected_options_list

    def check_multi_select_drop_down_values(self):
        data = []
        values = self.elements_are_visible(self.locators.MULTI_SELECT_DROP_DOWN_FIELD_OPTIONS_SELECTED)
        for value in values:
            data.append(value.text)
        return data


    def check_standard_multi_select(self):
        values = self.elements_are_present(self.locators.STANDARD_MULTI_SELECT_VALUES_LIST)
        colors_before = {}
        colors_after = {}
        checked_values = random.sample(values, k=(random.randint(1, 4)))
        self.key_down(Keys.CONTROL)
        for value in checked_values:
            colors_before[f'{value.text}'] = value.value_of_css_property('color')
            value.click()
            colors_after[f'{value.text}'] = value.value_of_css_property('color')
        self.key_up(Keys.CONTROL)
        return colors_before, colors_after


