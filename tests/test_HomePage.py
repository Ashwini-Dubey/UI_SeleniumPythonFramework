import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from ..utilities.BaseClass import BaseClass
from ..pageObjects.HomePage import HomePage
from ..TestData.HomePageData import HomePageData


class TestHomePage(BaseClass):


    def test_formSubmission(self,getData):
        """
        Test method for simulating an end-to-end user journey on the application.
        """

        homePage = HomePage(self.driver)
        log = self.getlogger()

        log.info(f"{getData["Name"]} is the name")
        # Name
        #driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys('Test')
        homePage.getName().send_keys(getData["Name"])

        # Email
        #driver.find_element(By.NAME, "email").send_keys("testing@yopmail.com")
        homePage.getName().send_keys(getData["Email"])

        # Password
        #driver.find_element(By.ID, "exampleInputPassword1").send_keys("Pass@1234")
        homePage.getPassword().send_keys(getData["Password"])

        # Checkbox
        #driver.find_element(By.ID, "exampleCheck1").click()
        homePage.clickCheckbox()

        #Gender
        #Gender = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
        #Gender.select_by_visible_text("Female")
        homePage.selectGender(getData["Gender"])

        # EmploymentStatus
        #driver.find_element(By.XPATH, "//input[@id='inlineRadio2']").click()
        homePage.getEmploymentStatus()

        # DOB
        #driver.find_element(By.NAME, "bday").send_keys('1996-01-01')
        homePage.getDOB().send_keys(getData["DOB"])

        # Submit
        #driver.find_element(By.XPATH, "//input[@type='submit']").click()
        homePage.clickSubmit()

        # Success Message
        #message = driver.find_element(By.CLASS_NAME, "alert-success").text
        #print(message)
        #assert "Success!" in message
        homePage.getSuccessMessage()
        log.info(homePage.getSuccessMessage())
        log.info("Registration is successful")
        self.driver.refresh()
        #assert "Success!" in success_message


#Invoking DDT
    #Tuple Data Set
    #@pytest.fixture(params=[("Test","testddt1@yopmail.com","Pass@123","Male","1996-01-01"),("Test2","testddt2@yopmail.com","Pass@123","Female","1986-01-01")])

    #Dictionary Data set
    #@pytest.fixture(params=[{"Name":"Test","Email":"testddt1@yopmail.com","Password":"Pass@123","Gender":"Male","DOB":"1996-01-01"},{"Name":"Test2","Email":"testddt2@yopmail.com","Password":"Pass@123","Gender":"Female","DOB":"1976-01-01"}])

    #Get the data from HomePageData file
    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self,request):
       return request.param

