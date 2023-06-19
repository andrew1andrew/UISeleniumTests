from Pages.Base_page import BasePage
from Pages.Main_page import MainPage
import allure



@allure.title("Тест 1 - ")
@allure.severity("blocker")
def test_one_employee(driver):
    base_page = BasePage(driver)
    base_page.go_to_site()
    main_page = MainPage(driver)
    main_page.text_box()
