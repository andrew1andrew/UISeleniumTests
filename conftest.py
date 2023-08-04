import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def driver():
    service = Service()
    options = webdriver.ChromeOptions()
    options.add_argument('lang=en-GB')
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()
