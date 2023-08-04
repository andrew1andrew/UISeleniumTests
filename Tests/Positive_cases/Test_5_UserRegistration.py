""""Выполнять регистрацию пользователя с помощью библиотеки faker"""
from Pages.Base_page import BasePage
from Pages.Main_page import MainPage
import allure


@allure.title("Test 5 - User registration")
@allure.severity("blocker")
def test_5(driver):
    with allure.step("Open the page"):
        base_page = BasePage(driver)
        base_page.go_to_site()
    with allure.step("Checking that "):
        main_page = MainPage(driver)
        main_page.user_registration(driver)
