from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException, NoSuchElementException
from typing import List, Optional


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.google.com/ncr"

    def go_to_site(self):
        return self.driver.get(self.url)

    def element_is_visible(self, locator: tuple, timeout=5) -> WebElement:
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator: tuple, timeout=5) -> List[WebElement]:
        return Wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def assert_element_is_visible(self, locator: tuple) -> Optional[WebElement]:
        try:
            element = Wait(self.driver, 5).until(EC.visibility_of_element_located(locator))
            return element
        except TimeoutException or NoSuchElementException:
            return None
