from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:
    NEW_TAB_BUTTON = (By.CSS_SELECTOR, 'button[id="tabButton"]')
    NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, 'button[id="windowButton"]')
    NEW_WINDOW_MESSAGE_BUTTON = (By.CSS_SELECTOR, 'button[id="messageWindowButton"]')
    NEW_TAB_MESSAGE = (By.CSS_SELECTOR, 'h1[id="sampleHeading"]')


class BrowserAlertsPageLocators:
    ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id="alertButton"]')
    APPEAR_ALERT_AFTER_FIVE_SECONDS_BUTTON = (By.CSS_SELECTOR, 'button[id="timerAlertButton"]')
    CONFIRM_ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id="confirmButton"]')
    CONFIRM_ALERT_RESULT = (By.CSS_SELECTOR, 'span[id="confirmResult"]')
    PROMPT_ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id="promtButton"]')
    PROMPT_ALERT_RESULT = (By.CSS_SELECTOR, 'span[id="promptResult"]')


class FramePageLocators:
    LARGE_FRAME = (By.CSS_SELECTOR, 'iframe[id="frame1"]')
    SMALL_FRAME = (By.CSS_SELECTOR, 'iframe[id="frame2"]')
    TITLE_IN_FRAME = (By.CSS_SELECTOR, 'h1[id="sampleHeading"]')
    TITLE_IN_FRAMES_PAGE = (By.CSS_SELECTOR, 'h1[class="text-center"]')


class NestedFramesPageLocators:
    TITLE = (By.CSS_SELECTOR, 'h1[class="text-center"]')
    PARENT_FRAME_TEXT = (By.CSS_SELECTOR, 'body')
    CHILD_FRAME_TEXT = (By.CSS_SELECTOR, 'p')
