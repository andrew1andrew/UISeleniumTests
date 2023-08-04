import allure

from Pages.Base_page import BasePage
from Locators.Page_locators import PageLocators as Locators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from faker import Faker
from random import randint
import pytest
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By


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

    def user_registration(self):
        self.element_is_visible(Locators.SIGN_IN_BUTTON).click()
        self.sleep()
        self.driver.find_elements(By.CSS_SELECTOR, "span[jsname='V67aGc']")[2].click()
        self.element_is_visible(Locators.BUTTON_FOR_PERSONAL_USE).click()
        self.sleep()
        with allure.step("Enter first and last name"):
            fake = Faker()
            self.element_is_visible(Locators.TEXT_INPUT).send_keys(fake.first_name())
            self.elements_are_visible(Locators.TEXT_INPUT)[1].send_keys(fake.last_name())
            self.element_is_visible(Locators.ELEMS_IN_SIGN_IN_PAGE).click()
        with allure.step("Enter date of birth and gender"):
            self.element_is_visible(Locators.NUM_INPUT).send_keys(randint(1, 28))
            self.driver.find_element(By.CSS_SELECTOR, f"option[value='{randint(1, 12)}']").click()
            self.elements_are_visible(Locators.NUM_INPUT)[1].send_keys(randint(1950, 2018))
            self.sleep()
            random_num = randint(1, 4)
            print(random_num)
            if random_num == 1 or 2 or 3:
                self.driver.find_element(By.CSS_SELECTOR, f"option[value='{random_num}']").click()
                self.element_is_visible(Locators.TEXT_INPUT).send_keys('Random gender')
                self.driver.find_element(By.CSS_SELECTOR, f"option[value='{random_num}']").click()
            else:
                self.driver.find_element(By.CSS_SELECTOR, f"option[value='{random_num}']").click()









