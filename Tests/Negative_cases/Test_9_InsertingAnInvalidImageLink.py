from Pages.Base_page import BasePage
from Pages.Main_page import MainPage
import allure


@allure.title("Test 9 - Inserting an invalid image link")
@allure.severity("critical")
def test_9(driver):
    with allure.step("Open the page"):
        base_page = BasePage(driver)
        base_page.go_to_site()
    with allure.step("Checking error text is visible"):
        main_page = MainPage(driver)
        main_page.invalid_image_link()
