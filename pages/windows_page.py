import time
from generator.generator import generated_person

from locators.windows_page_locators import BrowserWindowsPageLocators, BrowserAlertsPageLocators, FramePageLocators, \
    NestedFramesPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    def check_opened_new_tab_or_window(self, locator):
        self.element_is_visible(locator).click()
        self.switch_to_new_window()
        return self.element_is_visible(self.locators.NEW_TAB_MESSAGE).text


class BrowserAlertsPage(BasePage):
    locators = BrowserAlertsPageLocators()

    def click_on_button(self, locator):
        self.element_is_clickable(locator).click()

    def send_random_name_to_alert(self, alert):
        person = next(generated_person())
        name = person.full_name
        alert.send_keys(name)
        alert.accept()
        return name

    def check_prompt_result(self):
        return self.element_is_visible(self.locators.PROMPT_ALERT_RESULT).text

    def check_confirm_result(self):
        return self.element_is_visible(self.locators.CONFIRM_ALERT_RESULT).text


class FramePage(BasePage):
    locators = FramePageLocators()

    def get_title_text_on_frame(self):
        return self.element_is_visible(self.locators.TITLE_IN_FRAME).text

    def get_title_on_frames_page(self):
        return self.element_is_visible(self.locators.TITLE_IN_FRAMES_PAGE).text


class NestedFramesPage(BasePage):
    locators = NestedFramesPageLocators()

    def switch_to_child_frame(self):
        self.switch_to_default_content()
        self.switch_to_frame()
        self.switch_to_frame()

    def get_text_in_parent_frame(self):
        return self.element_is_present(self.locators.PARENT_FRAME_TEXT).text

    def get_text_in_child_frame(self):
        return self.element_is_present(self.locators.CHILD_FRAME_TEXT).text

    def get_title_text(self):
        return self.element_is_present(self.locators.TITLE).text