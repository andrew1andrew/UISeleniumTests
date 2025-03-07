from Pages.Base_page import BasePage
from Locators.Page_locators import PageLocators as Locators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MapsPage(BasePage):
    def non_existent_address_in_google_maps(self) -> str:
        maps_input = self.element_is_visible(Locators.INPUT_IN_GOOGLE_MAPS)
        maps_input.send_keys("qweasfdasfewqfqe")
        maps_input.send_keys(Keys.ENTER)
        error_text_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.TEXT_IN_GOOGLE_MAPS))
        return error_text_element.text
