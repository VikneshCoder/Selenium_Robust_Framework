import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):   # This is code get from the Pytest Doc to Select Browser in Cmd line (pytest --browser_name)
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope='class')
def LoginSetup(request):   # Browser Code Setup
    browser_name = request.config.getoption("browser_name")  # Code From Pytest DOC related to Browser
    if browser_name == "chrome":
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    else:
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    driver.maximize_window()
    request.cls.driver = driver   # Assigning Driver to the Class Object
    yield
    driver.quit()
