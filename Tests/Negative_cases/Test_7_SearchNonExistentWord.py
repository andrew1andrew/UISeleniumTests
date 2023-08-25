from Pages.Base_page import BasePage
from Pages.Main_page import MainPage
import allure


@allure.title("Test 7 - Search non existent word")
@allure.severity("normal")
def test_7(driver):
    with allure.step("Open the page"):
        base_page = BasePage(driver)
        base_page.go_to_site()
    with allure.step("Checking that the page with the SVG image will open and the search result will be zero"):
        main_page = MainPage(driver)
        main_page.search_non_existent_word(driver)
