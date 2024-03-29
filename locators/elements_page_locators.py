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


class ButtonsPageLocators:
    DOUBLE_CLICK_BUTTON = (By.CSS_SELECTOR, 'button[id="doubleClickBtn"]')
    RIGHT_CLICK_BUTTON = (By.CSS_SELECTOR, 'button[id="rightClickBtn"]')
    ALL_BUTTONS = (By.CSS_SELECTOR, '.mt-4 .btn-primary')

    # result
    DOUBLE_CLICK_TEXT = (By.CSS_SELECTOR, 'p[id="doubleClickMessage"]')
    RIGHT_CLICK_TEXT = (By.CSS_SELECTOR, 'p[id="rightClickMessage"]')
    CLICK_ME_TEXT = (By.CSS_SELECTOR, 'p[id="dynamicClickMessage"]')


class TestLinkPageLocators:
    LINK_HOME = (By.CSS_SELECTOR, 'a[id="simpleLink"]')
    LINK_DYNAMIC = (By.CSS_SELECTOR, 'a[id="dynamicLink"]')
    LINK_CREATE = (By.CSS_SELECTOR, 'a[id="dynamicLink"]')
    LINK_NO_CONTENT = (By.CSS_SELECTOR, 'a[id="no-content"]')
    LINK_MOVED = (By.CSS_SELECTOR, 'a[id="moved"]')
    LINK_BAD_REQUEST = (By.CSS_SELECTOR, 'a[id="bad-request"]')
    LINK_UNAUTHORIZED = (By.CSS_SELECTOR, 'a[id="unauthorized"]')
    LINK_FORBIDDEN = (By.CSS_SELECTOR, 'a[id="forbidden"]')
    LINK_NOT_FOUND = (By.CSS_SELECTOR, 'a[id="invalid-url"]')
    LINK_RESPONSE_TEXT = (By.CSS_SELECTOR, 'p[id="linkResponse"]')


class BrokenLinksAndImagesPageLocators:
    VALID_IMAGE = (By.CSS_SELECTOR, '.col-md-6 img[src="/images/Toolsqa.jpg"]')
    BROKEN_IMAGE = (By.CSS_SELECTOR, '.col-md-6 img[src="/images/Toolsqa_1.jpg"]')
    VALID_LINK = (By.CSS_SELECTOR, 'a[href="http://demoqa.com"]')
    BROKEN_LINK = (By.CSS_SELECTOR, 'a[href="http://the-internet.herokuapp.com/status_codes/500"]')


class UploadAndDownloadPageLocators:
    DOWNLOAD_BUTTON = (By.CSS_SELECTOR, 'a[id="downloadButton"]')
    UPLOAD_BUTTON = (By.CSS_SELECTOR, 'input[id="uploadFile"]')
    UPLOADED_RESULT = (By.CSS_SELECTOR, 'p[id="uploadedFilePath"]')


class DynamicPropertiesPageLocators:
    TEXT_WITH_RANDOM_ID = (By.CSS_SELECTOR, '.col-md-6 p')
    DISABLED_BUTTON = (By.CSS_SELECTOR, 'button[id="enableAfter"]')
    COLOR_CHANGE_BUTTON = (By.CSS_SELECTOR, 'button[id="colorChange"]')
    INVISIBLE_BUTTON = (By.CSS_SELECTOR, 'button[id="visibleAfter"]')
    HEADER_TEXT = (By.CSS_SELECTOR, 'h1[class="text-center"]')
