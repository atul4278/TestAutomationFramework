import logging

from selenium.common.exceptions import NoSuchElementException
from src.core.page import BasePage
from src.pages.product.locators import ProductPageLocators

from .locators import LoginPageLocators


class LoginPageActions(BasePage):
    def login(self, usr_name, pwd):
        self.send_keys(LoginPageLocators.inp_user_name, usr_name)
        self.send_keys(LoginPageLocators.inp_password, pwd)
        self.click(LoginPageLocators.btn_login)
