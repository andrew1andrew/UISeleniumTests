from Pages.Base_page import BasePage
from Locators.Page_locators import PageLocators as Locators
from selenium.webdriver.common.keys import Keys


class MapsPage(BasePage):
    def non_existent_address_in_google_maps(self):
        maps_input = self.element_is_visible(Locators.INPUT_IN_GOOGLE_MAPS)
        maps_input.send_keys("qweasfdasfewqfqe")
        maps_input.send_keys(Keys.ENTER)
        assert self.element_is_visible(Locators.TEXT_IN_GOOGLE_MAPS).text == "Google Maps can't find qweasfdasfewqfqe"