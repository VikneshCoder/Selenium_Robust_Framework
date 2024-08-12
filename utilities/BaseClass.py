import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures('LoginSetup')   # Common Reuse Code for Every Test Cases
class Baseclass:
    def Xpath_Waits(self, XPath):  # Waits
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, XPath))
        )

    def Implicit_Wait(self, Seconds):
        self.driver.implicitly_wait(Seconds)