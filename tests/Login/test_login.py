from pages.login.actions import LoginPageActions, LoginPageLocators
from pages.product.locators import ProductPageLocators
from selenium.common.exceptions import NoSuchElementException

class TestLogin:
    def test_successfull_login(self):
        page = LoginPageActions(self.driver)
        page.login(self.data['USERNAME'], self.data['PASSWORD'])
        exists = page.verify_element_exists(ProductPageLocators.page_header)
        if exists:
            page.log.info('Login successful and user navigated to Producsts page.')
        else:
            raise NoSuchElementException('Login failed. User not navigated to Products page.')

    def test_failed_login(self):
        page = LoginPageActions(self.driver)
        page.login(self.data['USERNAME'], 'asdafa')
        error_text = page.get_element_text(
            LoginPageLocators.txt_failed_login)

        if error_text in LoginPageLocators.error_msgs:
            page.log.info(
                'Login failed as expected. User not navigated to Products page.')
        else:
            raise AssertionError(
                'User should not be allowed to login. Check your creds.')

    def test_locked_user(self):
        page = LoginPageActions(self.driver)
        page.login('locked_out_user', self.data['PASSWORD'])
        error_text = page.get_element_text(
            LoginPageLocators.txt_failed_login)

        if error_text in LoginPageLocators.error_msgs:
            page.log.info(
                'Login failed as expected. User not navigated to Products page.')
        else:
            raise AssertionError(
                'User should not be allowed to login. Check your creds.')
