from Pages.Base_page import BasePage
from Pages.Main_page import MainPage
import allure


@allure.title("Test 6 - Search an empty string")
@allure.severity("normal")
def test_6(driver):
    with allure.step("Open the page"):
        base_page = BasePage(driver)
        base_page.go_to_site()
    with allure.step("Checking that the title will remain the same"):
        main_page = MainPage(driver)
        main_page.search_an_empty_string(driver)
