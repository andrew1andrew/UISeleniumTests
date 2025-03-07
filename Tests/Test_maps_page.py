import allure


@allure.title("Test 8 - Non-existent address in google maps")
@allure.severity("critical")
def test_non_existent_address_in_maps(driver, base_page, main_page, maps_page):

    with allure.step("Open the page"):
        base_page.go_to_site()

    with allure.step("Open the Google Maps"):
        main_page.go_to_the_google_maps()

    with allure.step("Checking that such an address does not exist"):
        error_text = maps_page.non_existent_address_in_google_maps()
        expected_error_text = "Google Maps can't find qweasfdasfewqfqe"
        assert error_text == expected_error_text, (
            f"Expected error text '{expected_error_text}', but got '{error_text}'")
