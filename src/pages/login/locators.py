from selenium.webdriver.common.by import By


class LoginPageLocators:
    inp_user_name = (By.ID, 'user-name')
    inp_password = (By.ID, 'password')
    btn_login = (By.ID, 'login-button')
    txt_failed_login = (By.TAG_NAME, 'h3')
    error_msgs = ['Epic sadface: Username is required', 'Epic sadface: Password is required',
                  'Epic sadface: Username and password do not match any user in this service']
