from Pages.Base_page import BasePage
from Locators.Page_locators import PageLocators as Locators
import pytest
import time


class MainPage(BasePage):

    # @pytest.fixture(scope=True)
    def text_box(self):
        self.element_is_visible(Locators.PAGES_BUT).click()
        time.sleep(2)
        self.element_is_visible(Locators.ELEMENTS_BUT).click()
        time.sleep(2)
