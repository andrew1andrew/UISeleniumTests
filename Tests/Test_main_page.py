import allure


@allure.title("Test 1 - Opening a google page")
@allure.severity("blocker")
def test_open_google_page(driver, base_page, main_page):

    with allure.step("Open the page"):
        base_page.go_to_site()

    with allure.step("Checking that the title is Google"):
        title = main_page.check_title(driver)
        assert title == "Google", f"Expected title 'Google', but got '{title}'. The page title is incorrect."


@allure.title("Test 2 - Correct display of the search result")
@allure.severity("blocker")
def test_search_result(driver, base_page, main_page):

    with allure.step("Open the page"):
        base_page.go_to_site()

    with allure.step("Checking that the page contains an image element with the weather and with a specific title"):
        title, image_element = main_page.search_result(driver)
        assert title == "Weather in Paris - Google Search", f"Expected title 'Weather in Paris - Google Search', \
                        but got '{title}'. The search result title is incorrect."
        assert image_element is not None, "The weather image element is not visible on the page."


@allure.title("Test 3 - Click on the first search result")
@allure.severity("critical")
def test_open_first_search_result(driver, base_page, main_page):

    with allure.step("Open the page"):
        base_page.go_to_site()

    with allure.step("Checking that clicking on the first search link will open a new window"):
        title = main_page.click_first_search_result(driver)
        assert title == "London - Wikipedia", f"Expected title 'London - Wikipedia', \
                        but got '{title}'. The first search result page did not open correctly."


@allure.title("Test 4 - Returning to the main page after clicking on the google logo")
@allure.severity("critical")
def test_return_to_the_main_page(driver, base_page, main_page):

    with allure.step("Open the page"):
        base_page.go_to_site()

    with allure.step("Checking that after clicking on the Google logo there will be a return to the main page"):
        title, logo_element = main_page.click_on_the_google_logo(driver)
        assert title == "Google", f"Expected title 'Google', but got '{title}'"
        assert logo_element is not None, "Google logo is not visible"


@allure.title("Test 5 - Search with an empty string")
@allure.severity("normal")
def test_search_with_an_empty_string(driver, base_page, main_page):

    with allure.step("Open the page"):
        base_page.go_to_site()

    with allure.step("Checking that the title will remain the same"):
        title = main_page.search_an_empty_string(driver)
        assert title == "Google", f"Expected title 'Google', but got '{title}'"


@allure.title("Test 6 - Search non existent word")
@allure.severity("normal")
def test_search_non_existent_word(driver, base_page, main_page):

    with allure.step("Open the page"):
        base_page.go_to_site()

    with allure.step("Checking that the page with the SVG image will open and the search result will be zero"):
        title, error_element, result = main_page.search_non_existent_word(driver)
        assert title == "sdasadjkqwasdvsdczxv - Google Search", f"Expected title 'sdasadjkqwasdvsdczxv - \
            Google Search', but got '{title}'"
        assert error_element is not None, "Error element is not visible"
        assert result == 0, f"Expected search result to be 0, but got {result}"


@allure.title("Test 7 - Inserting an invalid image link")
@allure.severity("critical")
def test_invalid_image_link(driver, base_page, main_page):

    with allure.step("Open the page"):
        base_page.go_to_site()

    with allure.step("Checking error text is visible"):
        error_text = main_page.invalid_image_link(driver)
        expected_error_text = "Can't use this link. Check that your link starts with \
            'http://' or 'https://' to try again."
        assert error_text == expected_error_text, f"Expected error text '{expected_error_text}', but got '{error_text}'"




