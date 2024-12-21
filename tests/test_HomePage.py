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

        # Name
        homePage.getName().send_keys(getData["Name"])

        #Email
        homePage.getName().send_keys(getData["Email"])

        #Password
        homePage.getPassword().send_keys(getData["Password"])

        #Checkbox
        homePage.clickCheckbox()

        #Gender
        homePage.selectGender(getData["Gender"])

        #EmploymentStatus
        homePage.getEmploymentStatus()

        #DOB
        homePage.getDOB().send_keys(getData["DOB"])

        #Submit
        homePage.clickSubmit()

        #Success Message
        homePage.getSuccessMessage()
        log.info(homePage.getSuccessMessage())
        log.info("Registration is successful")
        self.driver.refresh()



#Invoking DDT
    #Tuple Data Set
    #@pytest.fixture(params=[("Test","testddt1@yopmail.com","Pass@123","Male","1996-01-01"),("Test2","testddt2@yopmail.com","Pass@123","Female","1986-01-01")])
    #def getData(self,request):
    #   return request.param

    #Dictionary Data set
    @pytest.fixture(params=[{"Name":"Test","Email":"testddt1@yopmail.com","Password":"Pass@123","Gender":"Male","DOB":"1996-01-01"},{"Name":"Test2","Email":"testddt2@yopmail.com","Password":"Pass@123","Gender":"Female","DOB":"1976-01-01"}])
    def getData(self,request):
       return request.param

    #Get the data from HomePageData file
    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self,request):
       return request.param

