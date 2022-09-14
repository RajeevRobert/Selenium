from selenium.webdriver.common.by import By

class Test_LoginPage():
    username_id="Email"
    password_id="Password"
    login_XPATH="//button[normalize-space()='Log in']"
    logout_XPATH="//a[normalize-space()='Logout']"

    def __init__(self,driver):
        self.driver=driver

    def setUserName(self,username):
        self.driver.find_element(By.ID, self.username_id).clear()
        self.driver.find_element(By.ID,self.username_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.ID, self.password_id).clear()
        self.driver.find_element(By.ID,self.password_id).send_keys(password)

    def login(self):
        self.driver.find_element(By.XPATH, self.login_XPATH).click()

    def logout(self):
        self.driver.find_element(By.XPATH, self.logout_XPATH).click()

