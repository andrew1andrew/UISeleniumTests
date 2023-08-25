from Pages.Base_page import BasePage
from Pages.Account_page import AccountPage
import allure


@allure.title("Test 8 - Email login with empty data")
@allure.severity("blocker")
def test_8(driver):
    with allure.step("Open the page"):
        base_page = BasePage(driver)
        base_page.go_to_site()
    with allure.step("Checking that the text 'Enter an email or phone number' appears"):
        account_page = AccountPage(driver)
        account_page.login_by_mail_with_empty_date()
