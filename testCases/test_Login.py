from selenium import webdriver
import pytest
from pageObjects.LoginPage import Test_LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import pytest_html

class Test_Login():
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUsername()
    password=ReadConfig.getPassword()

    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.logger.info("*****************test_homePageTitle**********************")
        self.logger.info("*****************Home Page Title Verification**********************")
        #ser_obj = Service("C:\\Users\\user\\PycharmProjects\\UnitTestPOMSeleniumProject\\drivers\\chromedriver.exe")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_Title=self.driver.title
        if act_Title=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("*****************Home Page Title Verification Passed**********************")
        else:
            self.driver.save_screenshot("..\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error("*****************Home Page Title Verification Failed**********************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        #ser_obj = Service("C:\\Users\\user\\PycharmProjects\\UnitTestPOMSeleniumProject\\drivers\\chromedriver.exe")
        self.logger.info("*****************test_login**********************")
        self.logger.info("*****************Login Verification Started**********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=Test_LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.login()
        act_Title=self.driver.title
        if act_Title=="Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("*****************Login Verification Passed**********************")
        else:
            self.driver.save_screenshot("..\\Screenshots\\"+"test_login.png")
            self.driver.close()
            self.logger.info("*****************Login Verification Failed**********************")
            assert False

#Command to run script on specific browser
#pytest -v -s test_Login.py --browser chrome/firefox

#Parlell execution of testcases
#pytest -v -s -n=2 test_Login.py --browser chrome/firefox