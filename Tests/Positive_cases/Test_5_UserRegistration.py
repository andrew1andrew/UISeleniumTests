from Pages.Base_page import BasePage
from Pages.Account_page import AccountPage
import allure


@allure.title("Test 5 - User registration")
@allure.severity("blocker")
def test_5(driver):
    with allure.step("Open the page"):
        base_page = BasePage(driver)
        base_page.go_to_site()
    with allure.step("Checking user registration"):
        account_page = AccountPage(driver)
        account_page.user_registration()
