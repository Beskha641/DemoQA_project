from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def element_is_visible(self, locator, timeout=5):
        self.go_to_element(self.element_is_present(locator))
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
