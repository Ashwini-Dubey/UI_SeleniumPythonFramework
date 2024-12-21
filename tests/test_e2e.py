import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from ..pageObjects.CheckoutPage import CheckoutPage
from ..pageObjects.HomePage import HomePage
from ..pageObjects.ConfirmPage import ConfirmPage
from ..utilities.BaseClass import BaseClass
import pytest

class TestOne(BaseClass):
    """
    Test class for end-to-end testing of the application.
    """
    def test_e2e(self,getData):
        """
        Test method for simulating an end-to-end user journey on the application.
        """
        homePage = HomePage(self.driver)
        checkoutPage = CheckoutPage(self.driver)
        confirmPage = ConfirmPage(self.driver)
        log = self.getlogger()

        # Navigate to shop page
        homePage.shopItems().click()


        # Select products
        log.info("Adding all the products to the cart")
        for product in homePage.selectProducts():
            product.click()
        log.info("All the products are added to the cart")

        # Proceed to Checkout
        log.info("All the added products are available in the cart")
        checkoutPage.redirectToCheckout().click()
        time.sleep(10)

        # Locate and click the checkout button
        log.info("Ready to checkout the cart with the added products")
        checkoutPage.checkoutClick().click()
        time.sleep(10)

        #Search for the country and select 'India'

        confirmPage.countrySearch().send_keys(getData["Country"])
        confirmPage.countrySelect().click()

        # Agree to the terms and conditions
        confirmPage.checkTNC().click()

        # Complete the purchase
        log.info("Ready to make a purchase")
        confirmPage.clickPurchase().click()

        # Validate success message
        success = confirmPage.checkSuccessMessage().text
        assert "Success!" in success
        log.info("Congrats! Purchase is successful")
        self.driver.refresh()

    # Tuple Data Set
    #@pytest.fixture(params=[("Test"),("Test2")])
    #def getData(self, request):
    #   return request.param

    # Dictionary Data set
    @pytest.fixture(params=[{"Country": "Ind"},{"Country":"Ind"}])
    def getData(self, request):
        return request.param
