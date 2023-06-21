from selenium.webdriver.common.by import By


class PageLocators:
    PAGES_BUT = (By.CSS_SELECTOR, "div[class='avatar mx-auto white']")
    ELEMENTS_BUT = (By.CSS_SELECTOR, "li[class='btn btn-light ']")
    FULL_NAME = (By.CSS_SELECTOR, "input[placeholder*='Full Name']")
    EMAIL = (By.CSS_SELECTOR, "input[placeholder*='name@example.com']")
    ADDRESSES = (By.CSS_SELECTOR, "textarea[id*='Address']")
    BUTTON_SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")
    CREATED_TEXT_BOX = (By.CSS_SELECTOR, "div[class='border col-md-12 col-sm-12']")