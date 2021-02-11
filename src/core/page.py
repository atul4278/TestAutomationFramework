import os

import selenium.webdriver.support.expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from src.utilities.framework_logger import get_logger


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.test_name = os.environ.get(
            'PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
        self.log = get_logger(f'Log_{self.test_name}.log')

    def get(self, url):
        self.driver.get(url)
        self.log.info(f"Navigated to URL: {url}")

    def get_element(self, locator, timeout=30):
        element = WebDriverWait(self.driver, timeout=timeout).until(
            EC.element_to_be_clickable(locator))
        return element

    def click(self, locator, timeout=30):
        element = self.get_element(locator)
        element.click()
        self.log.info(f'Clicked on Element with locator: {locator}')

    def send_keys(self, locator, value, timeout=30):
        element = self.get_element(locator, timeout)
        element.send_keys(value)
        self.log.info(f'Set {value} on Element with locator: {locator}')

    def get_element_text(self, locator, timeout=30):
        element = self.get_element(locator, timeout)
        text = element.text
        self.log.info(f'Value {text} fetched from locator: {locator}')
        return text

    def verify_element_exists(self, locator, timeout=30):
        try:
            element = self.get_element(locator, timeout)
            if element:
                self.log.info(f'Element found with locator: {locator}')
                return True
        except NoSuchElementException:
            self.log.info(f'Element NOT found with locator: {locator}')
            return False
