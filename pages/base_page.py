import random
from datetime import datetime

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    @allure.step('Go to url')
    def open(self):
        self.browser.get(self.url)

    def element_is_visible(self, locator, timeout=5):
        self.go_to_element(self.element_is_present(locator, timeout))
        return wait(self.browser, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5):
        return wait(self.browser, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=5):
        return wait(self.browser, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=5):
        return wait(self.browser, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=5):
        return wait(self.browser, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=5):
        return wait(self.browser, timeout).until(EC.element_to_be_clickable(locator))

    def element_is_stationary(self, locator, timeout=5):
        element = self.element_is_present(locator)
        return wait(self.browser, timeout).until(
            lambda d: element.location == self.browser.find_element(*locator).location)

    def go_to_element(self, element):
        self.browser.execute_script("arguments[0].scrollIntoView();", element)

    def action_double_click(self, element):
        action = ActionChains(self.browser)
        action.double_click(element)
        action.perform()

    def action_right_click(self, element):
        action = ActionChains(self.browser)
        action.context_click(element)
        action.perform()

    def switch_to_new_window(self, num=1):
        assert num <= len(self.browser.window_handles), 'There is no window with this index'
        self.browser.switch_to.window(self.browser.window_handles[num])

    def switch_to_alert(self, timeout=5):
        wait(self.browser, timeout).until(EC.alert_is_present())
        return self.browser.switch_to.alert

    def get_alert_text(self, alert):
        return alert.text

    def switch_to_frame(self, num=0):
        return self.browser.switch_to.frame(self.browser.find_elements(By.TAG_NAME, "iframe")[num])

    def switch_to_parent_frame(self):
        self.browser.switch_to.parent_frame()

    def switch_to_default_content(self):
        self.browser.switch_to.default_content()

    def time_format_to_am_pm(self, time_str):
        time = datetime.strptime(time_str, "%H:%M")
        return time.strftime("%#I:%M %p")

    def drag_and_drop_by_offset(self, element, x_cord=0, y_cord=0):
        actions = ActionChains(self.browser)
        actions.drag_and_drop_by_offset(element, x_cord, y_cord)
        actions.perform()

    def drag_and_drop_to_element(self, element_what, element_where):
        actions = ActionChains(self.browser)
        actions.drag_and_drop(element_what, element_where)
        actions.perform()

    def move_mouse_to_element(self, element):
        actions = ActionChains(self.browser)
        actions.move_to_element(element)
        actions.perform()

    def key_down(self, key):
        actions = ActionChains(self.browser)
        actions.key_down(key)
        actions.perform()

    def key_up(self, key):
        actions = ActionChains(self.browser)
        actions.key_up(key)
        actions.perform()

    def get_element_area(self, element):
        location = element.location
        size = element.size
        x1, y1 = location['x'], location['y']
        x2, y2 = (x1 + size['width'], y1 + size['height'])
        return [x1, x2, y1, y2]

    def drag_and_drop_by_random_offset(self, element, min, max):
        actions = ActionChains(self.browser)
        x_offset = self.generate_random_offset_positive_or_negative(min, max)
        y_offset = self.generate_random_offset_positive_or_negative(min, max)
        actions.drag_and_drop_by_offset(element, x_offset, y_offset)
        actions.perform()
        return x_offset, y_offset

    def generate_random_offset_positive_or_negative(self, min, max):
        if random.choice([True, False]):
            return random.randint(min, max)
        else:
            return random.randint(-max, -min)

    def check_element_inside_another_element(self, element_inside, element_outside):
        inside_element_area = self.get_element_area(element_inside)
        outside_element_area = self.get_element_area(element_outside)
        return (outside_element_area[0] < inside_element_area[0] and
                outside_element_area[1] > inside_element_area[1] and
                outside_element_area[2] < inside_element_area[2] and
                outside_element_area[3] > inside_element_area[3])
