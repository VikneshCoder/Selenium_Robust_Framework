import pytest
from selenium.webdriver.common.by import By

from TestCaseData.Test_Case_Data_01 import TestDataOnce
from pageobjects.CartPage import Cart
from utilities.BaseClass import Baseclass


class TestCaseOne(Baseclass):  # From Utilities Imported Login Fixtures Without Writing This in Every Test Cases only Inherited Baseclass
    def test_one(self, getData):
        log = self.getLogger()
        Home = Cart(self.driver)  # Creating the Object for the class Cart
        initial_url = self.Main()
        Home.SearchItems().send_keys(getData["Search_Item"])   # Object calling class method
        products = Home.Products()
        log.info(f"The total products count is {len(products)}")
        buttons = Home.Buttons()
        log.info(f"The total Button count is {len(buttons)}")
        # //div[@class='products']//div[@class='product']//button[@type='button']/parent::div/parent::div/h44
        list_01 = []
        for button in buttons:
            list_01.append(button.find_element(By.XPATH, "parent::div/parent::div/h4").text)
            button.click()
        log.info(list_01)
        Count = Home.Product_Counts().text
        log.info(f"Total Product added in the cart is {Count}")
        assert len(products) == int(Count)

        Home.Cart_Click().click()
        checkOut = Home.Proceed_Button()

        self.Xpath_Waits("//input[@class='promoCode']")

        list_02 = []
        Veggies = checkOut.Get_Veg_Name()
        for Vegetables in Veggies:
            list_02.append(Vegetables.text)
        log.info(list_02)
        assert list_01 == list_02

        Total_Amount = checkOut.Total_Amount().text
        Int_Total_Amount = int(Total_Amount)

        checkOut.Apply_Promo_Code().send_keys("rahulshettyacademy")
        checkOut.Promo_Button().click()
        self.Implicit_Wait(8)
        Success_Message = checkOut.Success_Message().text
        assert "Code applied" in Success_Message

        Final = checkOut.Final_Amount().text
        Int_Final = float(Final)
        Discount_Amount = Int_Total_Amount * 0.10
        Final_Amount = Int_Total_Amount - Discount_Amount
        assert Final_Amount == Int_Final
        log.info(Discount_Amount)

        Products_amount = checkOut.Product_Amount()
        Amount = 0
        for Product_amount in Products_amount:
            Amount = Amount + int(Product_amount.text)
        log.info(Amount)
        assert Amount == Int_Total_Amount
        self.driver.get(initial_url)

    @pytest.fixture(params=TestDataOnce.TestDataExcel("Testcase_01"))
    def getData(self, request):
        return request.param