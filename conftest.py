import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import allure
import os
from Pages.Base_page import BasePage
from Pages.Main_page import MainPage
from Pages.Account_page import AccountPage
from Pages.Maps_page import MapsPage


@pytest.fixture()
def driver():
    service = Service()
    options = webdriver.ChromeOptions()
    options.add_argument('lang=en-GB')
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


# """"For docker"""
# @pytest.fixture()
# def driver():
#     service = Service()
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_argument('--no-sandbox')
#     chrome_options.add_argument('--headless')
#     chrome_options.add_argument('--disable-gpu')
#     chrome_options.add_argument('--disable-dev-shm-usage')
#     chrome_options.add_argument("--window-size=1920,1080")
#     driver = webdriver.Chrome(service=service, options=chrome_options)
#     yield driver
#     driver.quit()

@pytest.fixture(scope="function")
def base_page(driver):
    return BasePage(driver)


@pytest.fixture(scope="function")
def main_page(driver):
    return MainPage(driver)


@pytest.fixture(scope="function")
def account_page(driver):
    return AccountPage(driver)


@pytest.fixture(scope="function")
def maps_page(driver):
    return MapsPage(driver)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode) as f:
                if 'driver' in item.fixturenames:
                    web_driver = item.funcargs['driver']
                else:
                    print('Fail to take screen-shot')
                    return
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))
