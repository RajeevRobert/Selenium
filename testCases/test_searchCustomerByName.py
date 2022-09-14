import time
from pageObjects.LoginPage import Test_LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.SeachCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import pytest

class Test_SearchCustomerByName:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByName(self,setup):
        self.logger.info("*****************Test_SearchCustomerByName**********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp=Test_LoginPage(self.driver)
        self.lp.setPassword(self.username)
        self.lp.setPassword(self.password)
        self.lp.login()

        self.logger.info("*****************Login Successful**********************")
        self.logger.info("*****************Starting Searching Customer By Name**********************")

        self.addCustomer=AddCustomer(self.driver)
        self.addCustomer.clickOnCusotmerMenu()
        self.addCustomer.clickOnCustomerMenuItem()

        self.logger.info("*****************Searching Customer By Name**********************")
        searchCust=SearchCustomer(self.driver)
        searchCust.setFirstName("Saurav")
        searchCust.setLastName("Sharma")
        searchCust.clickSeach()
        status = searchCust.searchByName("Saurav Sharma")
        time.sleep(5)
        assert True == status
        self.logger.info("*****************Searching Customer By Name is Completed**********************")
        self.driver.close()


#Command to run script on specific browser
#pytest -v -s --html=seachCustomerByEmailReport.html testCases/test_addCustomerPage.py --browser chrome/firefox

#Parlell execution of testcases
#pytest -v -s -n=2 test_addCustomerPage.py --browser chrome/firefox
