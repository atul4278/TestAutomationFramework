from selenium import webdriver
import selenium.webdriver.support.expected_conditions as EC
from src.utilities.framework_logger import get_logger
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import logging



class BasePage:
    def __init__(self, driver):
        self.driver = driver
        # self.logger = get_logger('debug')
        
    def get(self, url):
        self.driver.get(url)
        logging.info(f"Navigated to URL: {url}")

    def get_element(self, locator, timeout=30):
        element = WebDriverWait(self.driver, timeout=timeout).until(EC.element_to_be_clickable(locator))
        return element
    
    def click(self, locator, timeout=30):
        element = self.get_element(locator)
        element.click()
        logging.info(f'Clicked on Element with locator: {locator}')

    def send_keys(self, locator, value, timeout=30):
        element = self.get_element(locator, timeout)
        element.send_keys(value)
        logging.info(f'Set {value} on Element with locator: {locator}')

    def get_element_text(self, locator, timeout=30):
        element = self.get_element(locator, timeout)
        text = element.text
        logging.info(f'Value {text} fetched from locator: {locator}')
        return text

    def verify_element_exists(self, locator, timeout=30):
            try:
                element = self.get_element(locator, timeout)
                if element:
                    logging.info(f'Element found with locator: {locator}')
                    return True
            except NoSuchElementException:
                logging.info(f'Element NOT found with locator: {locator}')
                return False