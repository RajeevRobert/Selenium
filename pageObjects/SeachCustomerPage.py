from selenium.webdriver.common.by import By
from selenium import webdriver

class SearchCustomer:
    txtSearch_email_ID="SearchEmail"
    txtFirst_Name_ID="SearchFirstName"
    txtLast_Name_ID="SearchLastName"
    btnSearch_ID="search-customers"

    tblCustomer_XPath="//table[@id='customers-grid']"
    tblRows_XPath="//table[@id='customers-grid']//tbody/tr"
    tblCol_XPath="//table[@id='customers-grid']//tbody/tr/td"
    tblSearch_Results="//table[@role='grid']"

    def __init__(self,driver):
        self.driver=driver

    def setEmail(self,email):
        self.driver.find_element(By.ID,self.txtSearch_email_ID).clear()
        self.driver.find_element(By.ID, self.txtSearch_email_ID).send_keys(email)

    def setFirstName(self,fname):
        self.driver.find_element(By.ID,self.txtFirst_Name_ID).clear()
        self.driver.find_element(By.ID, self.txtFirst_Name_ID).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.ID,self.txtLast_Name_ID).clear()
        self.driver.find_element(By.ID, self.txtLast_Name_ID).send_keys(lname)

    def clickSeach(self):
        self.driver.find_element(By.ID, self.btnSearch_ID).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH,self.tblRows_XPath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements(By.XPATH,self.tblCol_XPath))

    def searchByemail(self,email):
        flag=False
        for r in range(1,self.getNoOfRows()+1):
            table=self.driver.find_element(By.XPATH,self.tblCustomer_XPath)
            email_id=table.find_element(By.XPATH,"//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if email_id==email:
                flag=True
                break
        return flag

    def searchByName(self,name):
        flag=False
        for r in range(1,self.getNoOfRows()+1):
            table=self.driver.find_element(By.XPATH,self.tblCustomer_XPath)
            name_result=table.find_element(By.XPATH,"//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
            if name_result==name:
                flag=True
                break
        return flag




