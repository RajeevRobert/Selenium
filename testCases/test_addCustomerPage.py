import string
from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
from pageObjects.LoginPage import Test_LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.AddCustomerPage import AddCustomer
import pytest_html
import random

class Test_addCustomerPage():
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUsername()
    password=ReadConfig.getPassword()
    logger=LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self,setup):
        self.logger.info("*****************Test_addCustomerPage**********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp=Test_LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.login()
        self.logger.info("*****************Login Successful**********************")
        self.logger.info("*****************Started Add Customer testcase**********************")

        self.addCust=AddCustomer(self.driver)
        self.addCust.clickOnCusotmerMenu()
        self.addCust.clickOnCustomerMenuItem()
        self.addCust.clickOnAddNew()
        self.logger.info("*****************Customer Details**********************")
        self.email=random_generator()+"@gmail.com"
        self.addCust.setEmail(self.email)
        self.addCust.setPassowrd("Robby532*")
        self.addCust.setMgrOfVendor("Vendor 2")
        self.addCust.setGender("Male")
        self.addCust.setCompanyName("Accenture")
        self.addCust.setDOB("07/06/1991")
        self.addCust.setFirstName("Rajeev")
        self.addCust.setLastName("Komabthula")
        self.addCust.setAdminComment("It is a Testing Sample Run...")
        self.addCust.setCustomerRole("Guests")
        self.addCust.clickOnSave()
        self.logger.info("*****************Saving Customer Details**********************")
        self.logger.info("*****************Validating Customer**********************")
        self.msg=self.driver.find_element(By.TAG_NAME,"body").text
        #print(self.msg)

        if "customer has been added successfully." in self.msg:
            assert True
            self.logger.info("*****************Customer has been added successfully**********************")
        else:
            self.driver.save_screenshot(".\\Screenshots"+"test_addCustomer.png")
            self.logger.error("*****************Failed to add customer**********************")
            assert False

        self.driver.close()
        self.logger.info("*****************Test_addCustomerPage Testcase Completed**********************")

def random_generator(size=8,chars=string.ascii_lowercase + string.digits):
    return "".join(random.choice(chars)for i in range(size))


