from pages.Base_page import BasePage
from pages.Main_page import MainPage
import allure



@allure.title("Test 1 - Text box")
@allure.severity("critical")
def test_text_box(driver):
    with allure.step("Open the page"):
        base_page = BasePage(driver)
        base_page.go_to_site()
    with allure.step(""):
        main_page = MainPage(driver)
        main_page.text_box()
