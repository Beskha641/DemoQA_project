import time

import pytest
from pages.windows_page import BrowserWindowsPage, BrowserAlertsPage


class TestWindowsPage:
    class TestBrowserWindowsPage:

        def test_new_tab(self, browser):
            page = BrowserWindowsPage(browser, 'https://demoqa.com/browser-windows')
            page.open()
            text = page.check_opened_new_tab_or_window(page.locators.NEW_TAB_BUTTON)
            assert text == 'This is a sample page', "New tab didn't open"

        def test_new_window(self, browser):
            page = BrowserWindowsPage(browser, 'https://demoqa.com/browser-windows')
            page.open()
            text = page.check_opened_new_tab_or_window(page.locators.NEW_WINDOW_BUTTON)
            assert text == 'This is a sample page', "New window didn't open"

    class TestAlertsPage:

        def test_alert_button(self, browser):
            page = BrowserAlertsPage(browser, 'https://demoqa.com/alerts')
            page.open()
            page.click_on_button(page.locators.ALERT_BUTTON)
            alert = page.switch_to_alert()
            alert_text = page.get_alert_text(alert)
            alert.accept()
            assert alert_text == 'You clicked a button', 'Alert is not present'

        def test_appear_alert_after_five_seconds_button(self, browser):
            page = BrowserAlertsPage(browser, 'https://demoqa.com/alerts')
            page.open()
            page.click_on_button(page.locators.APPEAR_ALERT_AFTER_FIVE_SECONDS_BUTTON)
            alert = page.switch_to_alert(timeout=6)
            alert_text = page.get_alert_text(alert)
            alert.accept()
            assert alert_text == 'This alert appeared after 5 seconds', 'Alert is not present'

        def test_confirm_alert_button(self, browser):
            page = BrowserAlertsPage(browser, 'https://demoqa.com/alerts')
            page.open()
            page.click_on_button(page.locators.CONFIRM_ALERT_BUTTON)
            alert = page.switch_to_alert()
            alert_text = page.get_alert_text(alert)
            assert alert_text == 'Do you confirm action?', 'Alert is not present'
            alert.accept()
            result_text = page.check_confirm_result()
            print(result_text)
            assert 'Ok' in result_text, 'Alert does not confimed'

        def test_prompt_box_alert_button(self, browser):
            page = BrowserAlertsPage(browser, 'https://demoqa.com/alerts')
            page.open()
            page.click_on_button(page.locators.PROMPT_ALERT_BUTTON)
            alert = page.switch_to_alert()
            alert_text = page.get_alert_text(alert)
            assert alert_text == 'Please enter your name'
            random_person = page.send_random_name_to_alert(alert)
            result_text = page.check_prompt_result()
            print(result_text)
            assert random_person in result_text, 'Alert result does not match the sent value'
