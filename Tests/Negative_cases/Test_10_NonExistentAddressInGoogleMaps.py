from Pages.Base_page import BasePage
from Pages.Main_page import MainPage
from Pages.Maps_page import MapsPage
import allure


@allure.title("Test 10 - Non-existent address in google maps")
@allure.severity("critical")
def test_10(driver):
    with allure.step("Open the page"):
        base_page = BasePage(driver)
        base_page.go_to_site()
    with allure.step("Open the Google Maps"):
        main_page = MainPage(driver)
        main_page.go_to_the_google_maps()
    with allure.step("Checking that such an address does not exist"):
        maps_page = MapsPage(driver)
        maps_page.non_existent_address_in_google_maps()
