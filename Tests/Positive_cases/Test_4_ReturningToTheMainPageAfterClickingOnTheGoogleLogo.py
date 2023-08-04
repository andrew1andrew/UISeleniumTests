from Pages.Base_page import BasePage
from Pages.Main_page import MainPage
import allure


@allure.title("Test 4 - Returning to the main page after clicking on the google logo")
@allure.severity("critical")
def test_4(driver):
    with allure.step("Open the page"):
        base_page = BasePage(driver)
        base_page.go_to_site()
    with allure.step("Checking that after clicking on the Google logo there will be a return to the main page"):
        main_page = MainPage(driver)
        main_page.click_on_the_google_logo(driver)
