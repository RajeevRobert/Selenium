from selenium import webdriver
import pytest
#from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        ser_obj = Service("C:\\Users\\user\\PycharmProjects\\PythonPytestPOMHybridFramework\\drivers\\chromedriver.exe")
        driver = webdriver.Chrome(service=ser_obj)
        print("Launching Chrome browser..")
    elif browser=='firefox':
        ser_obj = Service("C:\\Users\\user\\PycharmProjects\\PythonPytestPOMHybridFramework\\drivers\\geckodriver.exe")
        driver = webdriver.Firefox(service=ser_obj)
        print("Launching Firefox browser..")
    return driver

def pytest_addoption(parser):   #This will get the value from CLI
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):#This will return browser value to setup method
    return request.config.getoption("--browser")

######Pytest HTML Report#################
#Hook adding env information in the report
def pytest_configure(config):
    config._metadata['Project Name']= 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Rajeev'

#Hook for delete/modify env info in the report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins", None)
