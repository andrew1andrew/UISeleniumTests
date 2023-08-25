import allure
from Pages.Base_page import BasePage
from Locators.Page_locators import PageLocators as Locators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import re


class MainPage(BasePage):

    @staticmethod
    def check_title(driver):
        assert driver.title == "Google"

    def find_in_search(self, subject):
        search_field = self.element_is_visible(Locators.SEARCH_FIELD)
        search_field.send_keys(subject)
        search_field.send_keys(Keys.ENTER)

    def search_result(self, driver):
        self.find_in_search("Weather in Paris")
        self.sleep()
        assert driver.title == "Weather in Paris - Google Search"
        assert self.assert_element_is_visible(Locators.IMAGE_WITH_WEATHER) is not None

    def click_first_search_result(self, driver):
        self.find_in_search("London")
        self.page_loading(driver)
        ActionChains(driver).move_to_element(self.element_is_visible(Locators.FIRST_SEARCH)).perform() # Moving the mouse to the first search result
        self.sleep()
        opening_the_first_search_page = self.element_is_visible(Locators.GO_TO_THE_FIRST_SEARCH)
        driver.execute_script('arguments[0].click();', opening_the_first_search_page)
        self.page_loading(driver)
        assert driver.title == "London - Wikipedia"

    def click_on_the_google_logo(self, driver):
        self.find_in_search("News")
        self.element_is_visible(Locators.GOOGLE_LOGO).click()
        self.sleep()
        assert driver.title == "Google"
        assert self.assert_element_is_visible(Locators.GOOGLE_LOGO) is None

    def search_an_empty_string(self, driver):
        self.find_in_search("")
        self.sleep()
        assert driver.title == "Google"

    def search_non_existent_word(self, driver):
        self.find_in_search("sdasadjkqwasdvsdczxv")
        self.sleep()
        assert driver.title == "sdasadjkqwasdvsdczxv - Google Search"
        assert self.assert_element_is_visible(Locators.SVG_ERROR_PAGE_OPENING) is not None
        with allure.step("Checking that the search result is zero"):
            result_stats = self.element_is_visible(Locators.RESULT_STATS).text
            matches = re.findall(r'\b\d+\b', result_stats)
            if matches:
                result = int(matches[0])
                assert result == 0

    def invalid_image_link(self):
        self.find_in_search("Photo")
        self.element_is_visible(Locators.GO_TO_IMAGE).click()
        self.element_is_visible(Locators.GOOGLE_LENS).click()
        self.element_is_visible(Locators.INPUT_GOOGLE_LENS).send_keys("hhttps://google.com")
        self.element_is_visible(Locators.SEARCH_GOOGLE_LENS).click()
        self.sleep()
        assert self.element_is_visible(Locators.ERROR_TEXT_GOOGLE_LENS).text == "Can't use this link. Check that your link starts with 'http://' or 'https://' to try again."

    def go_to_the_google_maps(self):
        self.find_in_search("Maps")
        self.element_is_visible(Locators.GOOGLE_MAPS).click()
        self.sleep()








