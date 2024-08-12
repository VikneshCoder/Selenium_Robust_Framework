from selenium.webdriver.common.by import By


class CheckOut:
    def __init__(self, driver):
        self.driver = driver

    Get_Veggies_Name = (By.CSS_SELECTOR, "p.product-name")
    def Get_Veg_Name(self):
        return self.driver.find_elements(*CheckOut.Get_Veggies_Name)

    Total_amount = (By.CSS_SELECTOR, "span.discountAmt")
    def Total_Amount(self):
        return self.driver.find_element(*CheckOut.Total_amount)

    Apply_Promo_code = (By.XPATH, "//input[@class='promoCode']")
    def Apply_Promo_Code(self):
        return self.driver.find_element(*CheckOut.Apply_Promo_code)

    Promo_button = (By.XPATH, "//button[@class='promoBtn']")
    def Promo_Button(self):
        return self.driver.find_element(*CheckOut.Promo_button)

    Success_message = (By.XPATH, "//span[@class='promoInfo']")
    def Success_Message(self):
        return self.driver.find_element(*CheckOut.Success_message)

    Final_amount = (By.CSS_SELECTOR, "span.discountAmt")
    def Final_Amount(self):
        return self.driver.find_element(*CheckOut.Final_amount)

    Product_amount = (By.XPATH, "//tbody/tr/td[5]/p")
    def Product_Amount(self):
        return self.driver.find_elements(*CheckOut.Product_amount)
