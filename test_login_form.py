from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLoginForm:
    LOGIN_INPUT = (By.ID, 'login-input')
    PASSWORD_INPUT = (By.ID, 'password-input')
    SUBMIT_BUTTON = (By.ID, 'submit-button')
    STATUS_MESSAGE = (By.ID, 'error-message')
    ERROR_WRONG_CREDENTIALS = 'Wrong login or password'
    ERROR_SHORT_PASSWORD = 'Password must be at least 6 characters'

    def set_up(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://qa-guru.github.io/one-page-form/login.html')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def tear_down(self):
        self.driver.quit()

    def input_login_form(self, login):
        input_login = self.driver.find_element(*self.LOGIN_INPUT)
        input_login.send_keys(login)

    def input_password_form(self, password):
        input_password = self.driver.find_element(*self.PASSWORD_INPUT)
        input_password.send_keys(password)

    def click_button(self):
        submit_button = self.driver.find_element(*self.SUBMIT_BUTTON)
        submit_button.click()

    def wait_for_status_message(self, text):
        return WebDriverWait(self.driver, 5).until(
            EC.text_to_be_present_in_element(self.STATUS_MESSAGE, text))

    def test_login_with_short_password(self):
        try:
            self.set_up()
            self.input_login_form('example')
            self.input_password_form('1')
            self.click_button()

            assert self.wait_for_status_message(self.ERROR_SHORT_PASSWORD)
        finally:
            self.tear_down()

    def test_invalid_login(self):
        try:
            self.set_up()
            self.input_login_form('Invalidy')
            self.input_password_form('123456')
            self.click_button()

            assert self.wait_for_status_message(self.ERROR_WRONG_CREDENTIALS)
        finally:
            self.tear_down()