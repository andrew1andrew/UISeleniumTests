from pages.Base_page import BasePage
from locators.Page_locators import PageLocators as Locators
import pytest
import time
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By


class MainPage(BasePage):

    def sleep(self):
        time.sleep(1)

    # @pytest.fixture(scope=True)
    def switch_to_activity(self, index):
        self.sleep()
        self.element_is_visible(Locators.PAGES_BUT).click()
        self.sleep()
        elem = self.driver.find_elements(By.CSS_SELECTOR, "li[class='btn btn-light ']")
        elem[index].click()
        self.sleep()

    def text_box(self):
        self.switch_to_activity(0)
        self.element_is_visible(Locators.FULL_NAME).send_keys("Andrew Andrew")
        self.element_is_visible(Locators.EMAIL).send_keys("andrew_andew@mail.com")
        self.element_is_visible(Locators.ADDRESSES).send_keys("95 Place du Jeu de Paume")
        self.elements_are_visible(Locators.ADDRESSES)[1].send_keys("72 Rue Hubert de Lisle")
        self.sleep()
        self.element_is_visible(Locators.BUTTON_SUBMIT).click()
        try:
            assert self.element_is_visible(Locators.CREATED_TEXT_BOX)
        except TimeoutException or NoSuchElementException:
            assert False



