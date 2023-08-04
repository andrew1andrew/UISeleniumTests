from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from Locators.Page_locators import PageLocators as Locators
from selenium.common import TimeoutException, NoSuchElementException
import time


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.google.com/"

    def go_to_site(self):
        return self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    ''''A function that will return an AssertionError if the element is not found and None is returned'''
    def assert_element_is_visible(self, locator):
        try:
            element = Wait(self.driver, 5).until(EC.visibility_of_element_located(locator))
            return element
        except TimeoutException or NoSuchElementException:
            return None

    ''''Checking until the page is fully loaded'''
    @staticmethod
    def page_loading(driver):
        Wait(driver, 30).until(lambda x: x.execute_script("return document.readyState === 'complete'"))

    @staticmethod
    def sleep():
        time.sleep(1)
