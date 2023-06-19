import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options



@pytest.fixture()
def driver():
    # options = Options()
    # options.add_argument("--force-device-scale-factor=0.9") # настройка масштабирования в хроме на 90%
    driver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service)
    yield driver
    driver.quit()
