from selenium.webdriver.common.by import By
from pageobjects.CheckOutPage import CheckOut


class Cart:
    def __init__(self, driver):
        self.driver = driver

    Search = (By.CSS_SELECTOR, "input[placeholder*='Search']")  # Search Box
    def SearchItems(self):
        return self.driver.find_element(*Cart.Search)

    Product = (By.XPATH, "//div[@class='product']")
    def Products(self):
        return self.driver.find_elements(*Cart.Product)

    Button = (By.XPATH, "//div[@class='products']//div[@class='product']//button[@type='button']")
    def Buttons(self):
        return self.driver.find_elements(*Cart.Button)

    Product_Count = (By.XPATH, "//tbody/tr[1]/td/strong")
    def Product_Counts(self):
        return self.driver.find_element(*Cart.Product_Count)

    CartClick = (By.CLASS_NAME, "cart-icon")
    def Cart_Click(self):
        return self.driver.find_element(*Cart.CartClick)

    Proceed_button = (By.XPATH, "//button[text()='PROCEED TO CHECKOUT']")
    def Proceed_Button(self):
        self.driver.find_element(*Cart.Proceed_button).click()
        checkOut = CheckOut(self.driver)  # Creating Next Page Object Here itself
        return checkOut   # Returning That Object here

