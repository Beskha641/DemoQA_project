import random

from selenium.webdriver.common.by import By


class PracticeFormPageLocators:
    # inputs
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, 'input[id="firstName"]')
    LAST_NAME_INPUT = (By.CSS_SELECTOR, 'input[id="lastName"]')
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    MOBILE_INPUT = (By.CSS_SELECTOR, 'input[id="userNumber"]')
    SUBJECTS_INPUT = (By.CSS_SELECTOR, 'input[id="subjectsInput"]')
    FILE_INPUT = (By.CSS_SELECTOR, 'input[id="uploadPicture"]')

    # other
    GENDER_RADIO_BUTTONS = (By.CSS_SELECTOR, 'div.custom-radio')
    HOBBIES_CHECKBOXES = (By.CSS_SELECTOR, 'label[for*="hobbies-checkbox"]')
    SELECT_STATE_INPUT = (By.CSS_SELECTOR, 'div[id="state"]')
    SELECT_STATE_OPTION = (By.CSS_SELECTOR, f'div[id="react-select-3-option-{random.randint(0,3)}"]')
    SELECT_CITY_INPUT = (By.CSS_SELECTOR, 'div[id="city"]')
    SELECT_CITY_OPTIONS = (By.CSS_SELECTOR, f'div[id*="react-select-4-option"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[id="submit"]')
    CURRENT_ADDRESS_INPUT = (By.CSS_SELECTOR, 'textarea[id="currentAddress"]')
    ADDRESS_VALUES = (By.CSS_SELECTOR, 'div[class*="singleValue"]')
    SUBMITTED_FORM_TITLE = (By.CSS_SELECTOR, 'div[id="example-modal-sizes-title-lg"]')
    SUBMITTED_FORM_LABELS = (By.CSS_SELECTOR, 'tbody>tr>:nth-child(1)')
    SUBMITTED_FORM_VALUES = (By.CSS_SELECTOR, 'tbody>tr>:nth-child(2)')


    # calendar
    DATE_OF_BIRTH_INPUT = (By.CSS_SELECTOR, 'input[id="dateOfBirthInput"]')
    CALENDAR_DAYS = (By.CSS_SELECTOR, 'div[class*="react-datepicker__day react-datepicker__day--"]:not(['
                                      'class*="react-datepicker__day--outside-month"])')
    CALENDAR_MONTH = (By.CSS_SELECTOR, 'select[class="react-datepicker__month-select"]')
    CALENDAR_YEAR = (By.CSS_SELECTOR, 'select[class="react-datepicker__year-select"]')
    SELECTED_MONTH_AND_YEAR = (By.CSS_SELECTOR, 'div.react-datepicker__current-month')


