from selenium.webdriver.common.by import By

class CheckoutPage:
    """
    Page Object class for the Checkout page.
    This class contains locators and methods related to the Checkout page elements and actions.
    """
    redirectCheckout = (By.XPATH, "//a[@class='nav-link btn btn-primary']")
    checkout = (By.XPATH, "//button[@class='btn btn-success']")

    def __init__(self, driver):
        """
        Initialize with the WebDriver instance.
        """
        self.driver = driver

    def redirectToCheckout(self):
        """
        Return the 'Proceed to Checkout' link element on the Checkout page.
        """
        return self.driver.find_element(*CheckoutPage.redirectCheckout)  # return 'Proceed to Checkout' link element

    def checkoutClick(self):
        """
        Return the 'Checkout' button element on the Checkout page.
        """
        return self.driver.find_element(*CheckoutPage.checkout)  # return 'Checkout' button element
