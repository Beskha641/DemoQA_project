import time

import pytest

from pages.windows_page import BrowserWindowsPage, BrowserAlertsPage, FramePage, NestedFramesPage, ModalDialogsPage


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

    class TestFramePage:
        @pytest.mark.parametrize('frame, width, height',
                                 [(0,'500px', '350px'),
                                  (1, '100px', '100px')])
        def test_switch_to_frames(self, browser, frame, width, height):
            page = FramePage(browser, 'https://demoqa.com/frames')
            page.open()
            checked_width, checked_height = page.check_frame_size(frame)
            page.switch_to_frame(frame)
            title_text = page.get_title_text_on_frame()
            assert title_text == 'This is a sample page', 'Switch into frame is not completed'
            assert checked_width == width and checked_height == height, 'Frame sizes does not match'

    class TestNestedFramesPage:

        def test_nested_frames(self, browser):
            page = NestedFramesPage(browser, 'https://demoqa.com/nestedframes')
            page.open()
            page.switch_to_frame()
            parent_frame_text = page.get_text_in_parent_frame()
            assert parent_frame_text == 'Parent frame', 'Switch into parent frame is not completed'
            page.switch_to_child_frame()
            child_frame_text = page.get_text_in_child_frame()
            assert child_frame_text == 'Child Iframe', 'Switch into child frame is not completed'
            page.switch_to_default_content()
            title_text = page.get_title_text()
            assert title_text == 'Nested Frames', 'Switch into page is not completed'

    class TestModalDialogsPage:

        def test_small_modal(self, browser):
            page = ModalDialogsPage(browser, 'https://demoqa.com/modal-dialogs')
            page.open()
            modal_title = page.check_modal_window('Small modal')
            assert modal_title == 'Small Modal'

        def test_large_modal(self, browser):
            page = ModalDialogsPage(browser, 'https://demoqa.com/modal-dialogs')
            page.open()
            modal_title = page.check_modal_window('Large modal')
            assert modal_title == 'Large Modal'
