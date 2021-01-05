import time
import logging
import pytest
from src.pages.login.actions import LoginPageActions, LoginPageLocators
from src.pages.Product.locators import ProductPageLocators
from src.utilities.framework_logger import get_logger


class TestLogin:
    def test_successfull_login(self, driver):
        page = LoginPageActions(driver)
        page.login('standard_user', 'secret_sauce')
        exists = page.verify_element_exists(ProductPageLocators.page_header)
        if exists:
            logging.info('Login successful and user navigated to Producsts page.')
        else:
            raise NoSuchElementException('Login failed. User not navigated to Products page.')

    def test_failed_login(self, driver):
        page = LoginPageActions(driver)
        page.login('standard_user', 'secret_sauce1')
        error_text = page.get_element_text(
            LoginPageLocators.txt_failed_login)

        if error_text in LoginPageLocators.error_msgs:
            logging.info(
                'Login failed as expected. User not navigated to Products page.')
        else:
            raise AssertionError(
                'User should not be allowed to login. Check your creds.')
