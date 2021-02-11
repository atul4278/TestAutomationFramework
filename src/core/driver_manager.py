"""
Make Sure to add drivers to PATH environment variable
MAC: 
brew install chromedriver
brew install geckodriver
"""
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class DriverManager:
    def get_driver(brwsr, remote=False):
        if remote:
            if brwsr.lower() == 'chrome':
                capabilities = DesiredCapabilities.CHROME.copy()
            elif brwsr.lower() == 'firefox':
                capabilities = DesiredCapabilities.FIREFOX.copy()
            driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=capabilities)
        else:
            if brwsr.lower() == 'chrome':
                driver = webdriver.Chrome()
            elif brwsr.lower() == 'firefox':
                driver = webdriver.Firefox()
        
        return driver
        