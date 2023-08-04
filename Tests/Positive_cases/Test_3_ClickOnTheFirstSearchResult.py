from Pages.Base_page import BasePage
from Pages.Main_page import MainPage
import allure


@allure.title("Test 3 - Click on the first search result")
@allure.severity("critical")
def test_3(driver):
    with allure.step("Open the page"):
        base_page = BasePage(driver)
        base_page.go_to_site()
    with allure.step("Checking that clicking on the first search link will open a new window"):
        main_page = MainPage(driver)
        main_page.click_first_search_result(driver)
