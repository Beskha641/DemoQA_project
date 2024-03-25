from locators.widgets_page_locators import WidgetsPageLocators
from pages.base_page import BasePage


class WidgetsPage(BasePage):
    locators = WidgetsPageLocators()

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