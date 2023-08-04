from Pages.Base_page import BasePage
from Pages.Main_page import MainPage
import allure


@allure.title("Test 2 - Correct display of the search result")
@allure.severity("blocker")
def test_2(driver):
    with allure.step("Open the page"):
        base_page = BasePage(driver)
        base_page.go_to_site()
    with allure.step("Checking that the page contains an image element with the weather and with a specific title"):
        main_page = MainPage(driver)
        main_page.search_result(driver)
