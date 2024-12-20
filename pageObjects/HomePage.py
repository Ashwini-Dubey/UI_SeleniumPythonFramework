from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class HomePage:
    """
    Page Object class for the Home page.
    This class contains locators and methods related to the Home page elements and actions.
    """
    shop = (By.XPATH, "//ul/li[2]")
    products = (By.XPATH, "//app-card//button")
    name = (By.CSS_SELECTOR,"input[name='name']")
    email = (By.NAME,"email")
    password = (By.ID,"exampleInputPassword1")
    checkbox = (By.ID,"exampleCheck1")
    gender = (By.ID,"exampleFormControlSelect1")
    selectGender = "Male"
    employment_status = (By.XPATH,"//input[@id='inlineRadio2']")
    dob = (By.NAME,"bday")
    submit = (By.XPATH,"//input[@type='submit']")
    success_message = (By.CLASS_NAME,"alert-success")

    def __init__(self, driver):
        """
        Initialize with the WebDriver instance.
        """
        self.driver = driver

    def shopItems(self):
        """
        Return the 'Shop' button element on the Home page.
        """
        return self.driver.find_element(*HomePage.shop)  # return the 'Shop' button web element

    def selectProducts(self):
        """
        Return a list of product elements on the Home page.
        """
        return self.driver.find_elements(*HomePage.products)  # return all product elements

    def getName(self):
        """
        Return the "Name" field element on the Home Page.
        """
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        """
        Return the "Email" field element on the Home Page.
        """
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        """
        Return the "Password" field element on the Home Page.
        """
        return self.driver.find_element(*HomePage.password)

    def clickCheckbox(self):
        """
        Return the "Checkbox" field element on the Home Page.
        """
        return self.driver.find_element(*HomePage.checkbox).click()

    def selectGender(self,text):
        """
        Return the "Gender" field element on the Home Page.
        """
        getGender = Select(self.driver.find_element(*HomePage.gender))
        return getGender.select_by_visible_text(text)

    def getEmploymentStatus(self):
        """
        Return the "Employment Status" field element on the Home Page.
        """
        return self.driver.find_element(*HomePage.employment_status).click()

    def getDOB(self):
        """
        Return the "DOB" field element on the Home Page.
        """
        return self.driver.find_element(*HomePage.dob)

    def clickSubmit(self):
        """
        Return the "Submit" button element on the Home Page.
        """
        return self.driver.find_element(*HomePage.submit).click()

    def getSuccessMessage(self):
        """
        Return the "Success Message" field element on the Home Page.
        """
        success_message = self.driver.find_element(*HomePage.success_message).text
        assert "Success!" in success_message
