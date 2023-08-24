from selenium.webdriver.common.by import By


class PageLocators:
    SEARCH_FIELD = (By.CSS_SELECTOR, "textarea[type='search']")
    IMAGE_WITH_WEATHER = (By.CSS_SELECTOR, "img[class='wob_tci']")
    FIRST_SEARCH = (By.CSS_SELECTOR, "div[class='TzHB6b cLjAic K7khPe']")
    GO_TO_THE_FIRST_SEARCH = (By.CSS_SELECTOR, "div[class*='TbwUpd NJj']")
    GOOGLE_LOGO = (By.CSS_SELECTOR, "a[title='Go to Google Home']")
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, "span[class*='gb']")
    ELEMS_GO_NEXT = (By.CSS_SELECTOR, "span[jsname='V67aGc']")
    BUTTON_FOR_PERSONAL_USE = (By.CSS_SELECTOR, "span[jsname='K4r5Ff']")
    TEXT_INPUT = (By.CSS_SELECTOR, "input[type='text']")
    NUM_INPUT = (By.CSS_SELECTOR, "input[type='tel']")
    DATE_LIST = (By.CSS_SELECTOR, "select[class='UDCCJb']")
    RADIO_BUTTON = (By.CSS_SELECTOR, "div[class='enBDyd ']")
    TEXT_CHOOSE_YOU_GMAIL_ADDRES = (By.CSS_SELECTOR, "span[jsslot]")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[type='password']")
    BUTTON_SKIP_NEXT = (By.CSS_SELECTOR, "button[class*='VfPpkd']")
    ELEM_IF_USERNAME_IS_TAKEN = (By.CSS_SELECTOR, "div[class*='o6c']")