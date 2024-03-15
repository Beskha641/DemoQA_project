from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    # form fields
    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    # created from
    CREATED_FULL_NAME = (By.CSS_SELECTOR, "#output #name")
    CREATED_EMAIL = (By.CSS_SELECTOR, "#output #email")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")


class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, 'button[title="Expand all"]')
    ITEMS_LIST = (By.CSS_SELECTOR, 'span[class="rct-title"]')
    CHECKED_ITEMS = (By.CSS_SELECTOR, 'svg[class="rct-icon rct-icon-check"]')
    TITLE_ITEM = (By.XPATH, './/ancestor::span[@class="rct-text"]')
    OUTPUT_RESULT = (By.CSS_SELECTOR, 'span[class="text-success"]')


class RadioButtonLocators:
    YES_RADIO_BUTTON = (By.CSS_SELECTOR, 'label[for="yesRadio"]')
    IMPRESSIVE_RADIO_BUTTON = (By.CSS_SELECTOR, 'label[for="impressiveRadio"]')
    NO_RADIO_BUTTON = (By.CSS_SELECTOR, 'label[for="noRadio"]')
    OUTPUT_RESULT = (By.CSS_SELECTOR, 'span[class="text-success"]')


class WebTablesLocators:
    # add person form
    ADD_BUTTON = (By.CSS_SELECTOR, 'button[id="addNewRecordButton"]')
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, 'input[id="firstName"]')
    LAST_NAME_INPUT = (By.CSS_SELECTOR, 'input[id="lastName"]')
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    AGE_INPUT = (By.CSS_SELECTOR, 'input[id="age"]')
    SALARY_INPUT = (By.CSS_SELECTOR, 'input[id="salary"]')
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, 'input[id="department"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[id="submit"]')

    # table
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[id="searchBox"]')
    HEADERS = (By.CSS_SELECTOR, 'div[class="rt-resizable-header-content"]')
    PREVIOUS_BUTTON = (By.CSS_SELECTOR, 'div[class="-previous"]')
    NEXT_BUTTON = (By.CSS_SELECTOR, 'div[class="-next"]')
    EDIT_BUTTONS = (By.CSS_SELECTOR, 'span[class="mr-2"]')
    FULL_PERSON_LIST = (By.CSS_SELECTOR, 'div[class="rt-tr-group"]')
    DELETE_BUTTONS = (By.CSS_SELECTOR, 'span[title="Delete"]')
    ROW_PARENT = (By.XPATH, './/ancestor::div[@class="rt-tr-group"]')
    SELECT_COUNT_ROWS = (By.CSS_SELECTOR, 'select[aria-label="rows per page"]')

    # edit form
    INPUT_FIELDS = (By.CSS_SELECTOR, 'div[class="mt-2 row"] input')
