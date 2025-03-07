from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.Base_page import BasePage
from Locators.Page_locators import PageLocators as Locators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import re
from faker import Faker


fake = Faker()


class MainPage(BasePage):

    @staticmethod
    def check_title(driver) -> str:
        return driver.title

    def find_in_search(self, subject: str):
        search_field = self.element_is_visible(Locators.SEARCH_FIELD)
        search_field.send_keys(subject)
        search_field.send_keys(Keys.ENTER)

    def search_result(self, driver) -> tuple[str, WebElement]:
        self.find_in_search("Weather in Paris")
        return driver.title, self.element_is_visible(Locators.IMAGE_WITH_WEATHER)

    def click_first_search_result(self, driver) -> str:
        self.find_in_search("London")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.FIRST_SEARCH))
        first_search_element = self.element_is_visible(Locators.FIRST_SEARCH)
        ActionChains(driver).move_to_element(first_search_element).perform()
        opening_the_first_search_page = self.element_is_visible(Locators.GO_TO_THE_FIRST_SEARCH)
        driver.execute_script('arguments[0].click();', opening_the_first_search_page)
        WebDriverWait(driver, 10).until(EC.title_contains("London"))
        return driver.title

    def click_on_the_google_logo(self, driver) -> tuple[str, WebElement]:
        self.find_in_search("News")
        self.element_is_visible(Locators.GOOGLE_LOGO).click()
        WebDriverWait(driver, 10).until(EC.title_is("Google"))
        return driver.title, self.element_is_visible(Locators.GOOGLE_LOGO)

    def search_an_empty_string(self, driver) -> str:
        self.find_in_search("")
        WebDriverWait(driver, 10).until(EC.title_is("Google"))
        return driver.title

    def search_non_existent_word(self, driver) -> tuple[str, WebElement, int]:
        self.find_in_search("sdasadjkqwasdvsdczxv")
        WebDriverWait(driver, 10).until(EC.title_is("sdasadjkqwasdvsdczxv - Google Search"))
        error_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.SVG_ERROR_PAGE_OPENING))
        result_stats = self.element_is_visible(Locators.RESULT_STATS).text
        matches = re.findall(r'\b\d+\b', result_stats)
        result = int(matches[0]) if matches else None
        return driver.title, error_element, result

    def invalid_image_link(self, driver) -> str:
        self.find_in_search("Photo")
        self.element_is_visible(Locators.GO_TO_IMAGE).click()
        self.element_is_visible(Locators.GOOGLE_LENS).click()
        self.element_is_visible(Locators.INPUT_GOOGLE_LENS).send_keys("hhttps://google.com")
        self.element_is_visible(Locators.SEARCH_GOOGLE_LENS).click()
        error_text_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.ERROR_TEXT_GOOGLE_LENS))
        return error_text_element.text

    def go_to_the_google_maps(self, driver) -> str:
        self.find_in_search("Maps")
        WebDriverWait(driver, 10).until(EC.title_contains("Google Maps"))
        return driver.title
