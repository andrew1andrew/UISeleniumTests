from Pages.Base_page import BasePage
from Pages.Main_page import MainPage
import allure


@allure.title("Test 1 - Opening a google page")
@allure.severity("blocker")
def test_1(driver):
    with allure.step("Open the page"):
        base_page = BasePage(driver)
        base_page.go_to_site()
    with allure.step("Checking that the title is Google"):
        main_page = MainPage(driver)
        main_page.check_title(driver)
