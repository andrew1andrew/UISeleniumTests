import allure
from Pages.Base_page import BasePage
from Locators.Page_locators import PageLocators as Locators
from faker import Faker
from random import randint
import time
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By


class AccountPage(BasePage):
    def go_to_the_account_page(self):
        self.element_is_visible(Locators.SIGN_IN_BUTTON).click()
        self.sleep()

    def user_registration(self):
        self.go_to_the_account_page()
        self.driver.find_elements(By.CSS_SELECTOR, "span[jsname*='V67']")[2].click()
        self.element_is_visible(Locators.BUTTON_FOR_PERSONAL_USE).click()
        self.sleep()
        with allure.step("Enter first and last name"):
            fake = Faker()
            self.element_is_visible(Locators.TEXT_INPUT).send_keys(fake.first_name())
            self.elements_are_visible(Locators.TEXT_INPUT)[1].send_keys(fake.last_name())
            self.element_is_visible(Locators.ELEMS_GO_NEXT).click()
        with allure.step("Enter date of birth and gender"):
            self.element_is_visible(Locators.NUM_INPUT).send_keys(randint(1, 28))
            self.driver.find_element(By.CSS_SELECTOR, f"option[value='{randint(1, 12)}']").click()
            self.elements_are_visible(Locators.NUM_INPUT)[1].send_keys(randint(1960, 2018))
            self.sleep()
            self.driver.find_elements(By.CSS_SELECTOR, f"option[value='{randint(1, 3)}']")[1].click()
            self.element_is_visible(Locators.ELEMS_GO_NEXT).click()
        with allure.step("Entering email"):
            self.generation_username()
            if self.assert_element_is_visible(Locators.ELEM_IF_USERNAME_IS_TAKEN) is not None:
                self.generation_username()
        with allure.step("Entering password"):
            password = fake.password()
            self.element_is_visible(Locators.PASSWORD_INPUT).send_keys(password)
            self.elements_are_visible(Locators.PASSWORD_INPUT)[1].send_keys(password)
            self.element_is_visible(Locators.ELEMS_GO_NEXT).click()
            self.sleep()

    def generation_username(self):
        try:
            fake = Faker()
            email = fake.free_email().split("@")
            self.element_is_visible(Locators.TEXT_INPUT).clear()
            self.element_is_visible(Locators.TEXT_INPUT).send_keys(email[0] + email[0])
        except TimeoutException or NoSuchElementException:
            self.driver.find_element(By.CSS_SELECTOR, "div[class='enBDyd ']").click()
        self.sleep()
        self.element_is_visible(Locators.ELEMS_GO_NEXT).click()

    def login_by_mail_with_empty_date(self):
        self.go_to_the_account_page()
        self.element_is_visible(Locators.GO_NEXT).click()
        self.sleep()
        assert self.element_is_visible(Locators.ELEM_IF_USERNAME_IS_TAKEN).text == "Enter an email or phone number"
