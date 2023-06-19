from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from Locators.Page_locators import PageLocators as Locators


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/"

    def element_is_visible(self, locator, timeout=3):
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=3):
        return Wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def go_to_site(self):
        return self.driver.get(self.url)