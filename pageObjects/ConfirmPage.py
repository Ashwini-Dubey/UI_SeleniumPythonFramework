from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ConfirmPage:
    """
    Page Object class for the Confirmation page.
    This class contains locators and methods related to the Confirmation page elements and actions.
    """
    searchCountry = (By.ID, "country")
    selectCountry = (By.LINK_TEXT, "India")
    tnc = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchaseButton = (By.XPATH, "//input[@type='submit']")
    successMessage = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def __init__(self, driver):
        """
        Initialize with the WebDriver instance.
        """
        self.driver = driver

    def countrySearch(self):
        """
        Return the input field for country search on the Confirmation page.
        """
        return self.driver.find_element(*ConfirmPage.searchCountry)  # return country search input element

    def countrySelect(self):
        """
        Return the 'India' option in the dropdown.
        Waits until the 'India' option is present on the page before returning it.
        """
        wait = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((ConfirmPage.selectCountry)))
        return self.driver.find_element(*ConfirmPage.selectCountry)  # return 'India' option element

    def checkTNC(self):
        """
        Return the Terms and Conditions checkbox element.
        """
        return self.driver.find_element(*ConfirmPage.tnc)  # return TnC checkbox element

    def clickPurchase(self):
        """
        Return the 'Purchase' button element on the Confirmation page.
        """
        return self.driver.find_element(*ConfirmPage.purchaseButton)  # return 'Purchase' button element

    def checkSuccessMessage(self):
        """
        Return the success message element after purchase.
        """
        return self.driver.find_element(*ConfirmPage.successMessage)  # return success message element
