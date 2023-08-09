import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


# @pytest.fixture()
# def driver():
#     service = Service()
#     options = webdriver.ChromeOptions()
#     options.add_argument('lang=en-GB')
#     driver = webdriver.Chrome(service=service, options=options)
#     yield driver
#     driver.quit()

""""For docker"""
@pytest.fixture()
def driver():
    service = Service()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()

