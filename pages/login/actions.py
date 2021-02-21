import logging

from selenium.common.exceptions import NoSuchElementException
from core.page import BasePage
from pages.product.locators import ProductPageLocators

from .locators import LoginPageLocators


class LoginPageActions(BasePage):
    def login(self, usr_name, pwd):
        self.send_keys(LoginPageLocators.inp_user_name, usr_name)
        self.send_keys(LoginPageLocators.inp_password, pwd)
        self.click(LoginPageLocators.btn_login)
