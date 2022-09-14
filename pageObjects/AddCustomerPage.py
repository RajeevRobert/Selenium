import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

class AddCustomer:
    lnkCustomer_menu_XPATH="//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomer_menuitem_XPATH="//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddnew_XPATH="//a[normalize-space()='Add new']"
    txtMail_XPATH="//input[@id='Email']"
    txtPassword_XPATH="//input[@id='Password']"
    txtFirstName_XPATH="//input[@id='FirstName']"
    txtLastName_XPATH="//input[@id='LastName']"
    rdMale_XPATH="//input[@id='Gender_Male']"
    rdFemale_XPATH="//input[@id='Gender_Female']"
    txtDOB_XPATH="//input[@id='DateOfBirth']"
    txtCompany_XPATH="//input[@id='Company']"
    cbTaxExempt_XPATH="//input[@id='IsTaxExempt']"
    txtNewsLetter_XPATH="//select[@id='SelectedNewsletterSubscriptionStoreIds']"
    txtCustomRoles_XPATH="//div[@class='input-group-append input-group-required']//div[@role='listbox']"
    lstitemRegistered_XPATH="//li[contains(text(),'Registered')]"
    lstitemAdministrator_XPATH="//li[contains(text(),'Administrators')]"
    lstitemVendors_XPATH="//li[contains(text(),'Vendors')]"
    lstitemGuests_XPATH="//li[contains(text(),'Guests')]"
    drpMgrofVendor_XPATH="//select[@id='VendorId']"
    txtAdminCmt_XPATH="//textarea[@id='AdminComment']"
    btnSave_XPATH="//button[@name='save']"

    def __init__(self,driver):
        self.driver=driver

    def clickOnCusotmerMenu(self):
        self.driver.find_element(By.XPATH,self.lnkCustomer_menu_XPATH).click()

    def clickOnCustomerMenuItem(self):
        self.driver.find_element(By.XPATH,self.lnkCustomer_menuitem_XPATH).click()

    def clickOnAddNew(self):
        self.driver.find_element(By.XPATH,self.btnAddnew_XPATH).click()

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.txtMail_XPATH).send_keys(email)

    def setPassowrd(self,password):
        self.driver.find_element(By.XPATH,self.txtPassword_XPATH).send_keys(password)

    def setFirstName(self,firstname):
        self.driver.find_element(By.XPATH,self.txtFirstName_XPATH).send_keys(firstname)

    def setLastName(self,lastname):
        self.driver.find_element(By.XPATH,self.txtLastName_XPATH).send_keys(lastname)

    def setCompanyName(self,cname):
        self.driver.find_element(By.XPATH,self.txtCompany_XPATH).send_keys(cname)

    def setDOB(self,dob):
        self.driver.find_element(By.XPATH,self.txtDOB_XPATH).send_keys(dob)

    def setAdminComment(self,cmnt):
        self.driver.find_element(By.XPATH,self.txtAdminCmt_XPATH).send_keys(cmnt)

    def setCustomerRole(self,role):
        self.driver.find_element(By.XPATH,self.txtCustomRoles_XPATH).click()
        time.sleep(5)
        if role=="Registered":
            self.listItem=self.driver.find_element(By.XPATH,self.lstitemRegistered_XPATH)
        elif role=="Administrators":
            self.listItem = self.driver.find_element(By.XPATH, self.lstitemAdministrator_XPATH)
        elif role=="Guests":
            time.sleep(5)
            self.driver.find_element(By.XPATH, "//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listItem = self.driver.find_element(By.XPATH, self.lstitemGuests_XPATH)
        elif role=="Registered":
            self.listItem = self.driver.find_element(By.XPATH, self.lstitemRegistered_XPATH)
        elif role=="Vendors":
            self.listItem = self.driver.find_element(By.XPATH, self.lstitemVendors_XPATH)
        else:
            self.driver.find_element(By.XPATH, self.lstitemGuests_XPATH)
        time.sleep(5)
        self.driver.execute_script("arguments[0].click();",self.listItem)

    def setMgrOfVendor(self,value):
        drp=Select(self.driver.find_element(By.XPATH,self.drpMgrofVendor_XPATH))
        drp.select_by_visible_text(value)

    def setGender(self,gender):
        if gender=="Male":
            self.driver.find_element(By.XPATH,self.rdMale_XPATH).click()
        elif gender=="Female":
            self.driver.find_element(By.XPATH, self.rdFemale_XPATH).click()
        else:
            self.driver.find_element(By.XPATH, self.rdMale_XPATH).click()
    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btnSave_XPATH).click()




