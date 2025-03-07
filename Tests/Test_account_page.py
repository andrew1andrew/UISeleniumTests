import allure


@allure.title("Test 9 - User registration")
@allure.severity("blocker")
def test_user_registration(driver, base_page, account_page):
    with allure.step("Open the page"):
        base_page.go_to_site()

    with allure.step("Checking user registration"):
        account_page.user_registration()
        assert "myaccount.google.com" in driver.current_url, "Registration failed, user not redirected to account page"


@allure.title("Test 10 - Email login with empty data")
@allure.severity("blocker")
def test_login_with_empty_data(driver, base_page, account_page):
    with allure.step("Open the page"):
        base_page.go_to_site()

    with allure.step("Checking that the text 'Enter an email or phone number' appears"):
        error_message = account_page.login_by_mail_with_empty_date()
        assert error_message == "Enter an email or phone number"
