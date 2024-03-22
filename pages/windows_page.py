import time
from generator.generator import generated_person

from locators.windows_page_locators import BrowserWindowsPageLocators, BrowserAlertsPageLocators
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

