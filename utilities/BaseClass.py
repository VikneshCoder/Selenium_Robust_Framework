import inspect
import logging
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC





@pytest.mark.usefixtures('LoginSetup')   # Common Reuse Code for Every Test Cases
class Baseclass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger

    def Xpath_Waits(self, XPath):  # Waits
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, XPath))
        )

    def Implicit_Wait(self, Seconds):
        self.driver.implicitly_wait(Seconds)

    def Main(self):
        return "https://rahulshettyacademy.com/seleniumPractise/#/"



