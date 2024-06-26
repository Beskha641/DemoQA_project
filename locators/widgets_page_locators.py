from selenium.webdriver.common.by import By


class AccordianPageLocators:
    SELECTION_HEADING_FIRST = (By.CSS_SELECTOR, 'div[id="section1Heading"]')
    SELECTION_CONTENT_FIRST = (By.CSS_SELECTOR, 'div[id="section1Content"] p')
    SELECTION_HEADING_SECOND = (By.CSS_SELECTOR, 'div[id="section2Heading"]')
    SELECTION_CONTENT_SECOND = (By.CSS_SELECTOR, 'div[id="section2Content"] p')
    SELECTION_HEADING_THIRD = (By.CSS_SELECTOR, 'div[id="section3Heading"]')
    SELECTION_CONTENT_THIRD = (By.CSS_SELECTOR, 'div[id="section3Content"] p')


class AutoCompletePageLocators:
    MULTI_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteMultipleInput"]')
    MULTI_INPUT_VALUES = (By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue auto-complete__multi-value"]')
    MULTI_INPUT_DELETE_BUTTONS = (By.CSS_SELECTOR, 'div[class="css-xb97g8 auto-complete__multi-value__remove"]')
    MULTI_INPUT_DELETE_ALL_BUTTON = (By.CSS_SELECTOR, 'div[class="auto-complete__indicators css-1wy0on6"]')

    SINGLE_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteSingleInput"]')
    SINGLE_INPUT_VALUE = (By.CSS_SELECTOR, 'div[class="auto-complete__single-value css-1uccc91-singleValue"]')


class DatePickerPageLocators:
    # Date picker
    DATE_SELECT = (By.CSS_SELECTOR, 'input[id="datePickerMonthYearInput"]')
    DATE_SELECT_MONTH = (By.CSS_SELECTOR, 'select[class="react-datepicker__month-select"]')
    DATE_SELECT_YEAR = (By.CSS_SELECTOR, 'select[class="react-datepicker__year-select"]')
    DATE_SELECT_DAYS_LIST = (By.CSS_SELECTOR, 'div[class*="react-datepicker__day react-datepicker__day--"]:not(['
                                              'class*="react-datepicker__day--outside-month"])')

    # Date and time picker
    DATE_AND_TIME_SELECT = (By.CSS_SELECTOR, 'input[id="dateAndTimePickerInput"]')
    DATE_AND_TIME_SELECT_MONTH = (By.CSS_SELECTOR, 'span[class="react-datepicker__month-read-view--selected-month"]')
    DATE_AND_TIME_SELECT_MONTH_LIST = (By.CSS_SELECTOR, 'div[class="react-datepicker__month-option"]')
    DATE_AND_TIME_SELECT_YEAR = (By.CSS_SELECTOR, 'span[class="react-datepicker__year-read-view--selected-year"]')
    DATE_AND_TIME_SELECT_YEAR_LIST = (By.CSS_SELECTOR, 'div[class*="react-datepicker__year-option"]')
    DATE_AND_TIME_SELECT_TIME_LIST = (By.CSS_SELECTOR, 'li[class*="react-datepicker__time-list-item "]')


class SliderPageLocators:
    SLIDER_BAR = (By.CSS_SELECTOR, 'input[class="range-slider range-slider--primary"]')
    SLIDER_VALUE = (By.CSS_SELECTOR, 'input[id="sliderValue"]')


class ProgressBarPageLocators:
    PROGRESS_BAR_BUTTON = (By.CSS_SELECTOR, 'button[id="startStopButton"]')
    PROGRESS_BAR = (By.CSS_SELECTOR, 'div[class="progress-bar bg-info"]')


class TabsPageLocators:
    WHAT_TAB = (By.CSS_SELECTOR, 'a[id="demo-tab-what"]')
    ORIGIN_TAB = (By.CSS_SELECTOR, 'a[id="demo-tab-origin"]')
    USE_TAB = (By.CSS_SELECTOR, 'a[id="demo-tab-use"]')
    MORE_TAB = (By.CSS_SELECTOR, 'a[id="demo-tab-more"]')
    WHAT_TAB_TEXT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-what"] p')
    ORIGIN_TAB_TEXT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-origin"] p')
    USE_TAB_TEXT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-use"] p')
    MORE_TAB_TEXT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-more"] p')


class ToolTipsPageLocators:
    POP_UP_MESSAGE = (By.CSS_SELECTOR, 'div[class="tooltip-inner"]')
    BUTTON = (By.CSS_SELECTOR, 'button[id="toolTipButton"]')
    INPUT_FIELD = (By.CSS_SELECTOR, 'input[id="toolTipTextField"]')
    HOVER_TEXT_LIST = (By.CSS_SELECTOR, 'div[id="texToolTopContainer"] a')


class MenuPageLocators:
    MAIN_ITEM_TWO = (By.LINK_TEXT, 'Main Item 2')
    MAIN_ITEM_ONE = (By.LINK_TEXT, 'Main Item 1')
    MAIN_ITEM_THREE = (By.LINK_TEXT, 'Main Item 3')


class SelectMenuPageLocators:
    REACT_SELECT_FIELD_LIST = (By.CSS_SELECTOR, '.col-sm-12 [class*="container"] svg')
    REACT_SELECT_OPTIONS = (By.CSS_SELECTOR, 'div[class*="option"]')
    SELECT_VALUE_FIELD_SELECTED_VALUE = (By.CSS_SELECTOR, '#withOptGroup [class*="singleValue"]')
    SELECT_ONE_FIELD_SELECTED_VALUE = (By.CSS_SELECTOR, '#selectOne [class*="singleValue"]')
    OLD_STYLE_SELECT_MENU = (By.CSS_SELECTOR, 'select[id="oldSelectMenu"]')
    MULTI_SELECT_DROP_DOWN_FIELD_OPTIONS_SELECTED = (By.CSS_SELECTOR, 'div[class="css-12jo7m5"]')
    STANDARD_MULTI_SELECT_VALUES_LIST = (By.CSS_SELECTOR, 'select[id="cars"] option')



