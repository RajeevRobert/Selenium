import time

from selenium import webdriver
import pytest
from pageObjects.LoginPage import Test_LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import pytest_html
from utilities import excelUtility

class Test_Login_DDT():
    baseURL=ReadConfig.getApplicationURL()
    path="C:\\Users\\user\\PycharmProjects\\PythonPytestPOMHybridFramework\\TestData\\data.xlsx"
    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_login_DDT(self,setup):
        #ser_obj = Service("C:\\Users\\user\\PycharmProjects\\UnitTestPOMSeleniumProject\\drivers\\chromedriver.exe")
        self.logger.info("*****************test_login_DDT**********************")
        self.logger.info("*****************Login Verification Started**********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=Test_LoginPage(self.driver)
        self.driver.implicitly_wait(10)

        self.rows=excelUtility.getRowCount(self.path,'robb')
        print("No of Rows:",self.rows)

        ddt_status=[]

        for r in range(2,self.rows+1):
            self.username=excelUtility.readData(self.path,'robb',r,1)
            self.password = excelUtility.readData(self.path, 'robb', r, 2)
            self.exp_value = excelUtility.readData(self.path, 'robb', r, 3)

            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.login()
            #time.sleep(5)

            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"

            if act_title==exp_title:
                if self.exp_value=="Passed":
                    self.logger.info("*******Passed*******")
                    time.sleep(5)
                    self.lp.logout()
                    ddt_status.append("Passed")
                elif self.exp_value=="Failed":
                    self.logger.info("*******Failed*******")
                    time.sleep(5)
                    self.lp.logout()
                    ddt_status.append("Failed")
            elif act_title!=exp_title:
                if self.exp_value=="Passed":
                    self.logger.info("*******Failed*******")
                    ddt_status.append("Failed")
                elif self.exp_value=="Failed":
                    self.logger.info("*******Passed*******")
                    ddt_status.append("Passed")

        if "Failed" not in ddt_status:
            self.logger.info("DDT Passed")
            self.driver.close()
            assert True
        else:
            self.logger.info("DDT Failed")
            self.driver.close()
            assert False

        self.logger.info("******End of test_login_DDT*********")
        self.logger.info("******Completed test_login_DDT*********")

#Command to run script on specific browser
#pytest -v -s test_login_DDT.py --browser chrome/firefox

#Parlell execution of testcases
#pytest -v -s -n=2 test_Login.py --browser chrome/firefox