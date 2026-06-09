from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestLoginForm:
    LOGIN_INPUT = (By.ID, 'login-input')
    PASSWORD_INPUT = (By.ID, 'password-input')
    SUBMIT_BUTTON = (By.ID, 'submit-button')
    STATUS_MESSAGE = (By.ID, 'error-message')
    ERROR_WRONG_CREDENTIALS = 'Wrong login or password'
    ERROR_SHORT_PASSWORD = 'Password must be at least 6 characters'
    ERROR_SHORT_LOGIN = 'Login is required (minimum 3 characters)'

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
        return WebDriverWait(
            self.driver,
            timeout=5,
            poll_frequency=0.5
        ).until(
            ec.text_to_be_present_in_element(
                self.STATUS_MESSAGE,
                text
            )
        )

    def test_login_with_short_password(self):
        login = 'example'
        password = '1'

        try:
            self.set_up()
            self.input_login_form(login)
            self.input_password_form(password)
            self.click_button()

            assert self.wait_for_status_message(self.ERROR_SHORT_PASSWORD)
        finally:
            self.tear_down()

    def test_empty_password(self):
        login = 'example'
        password = ''

        try:
            self.set_up()
            self.input_login_form(login)
            self.input_password_form(password)
            self.click_button()

            assert self.wait_for_status_message(self.ERROR_SHORT_PASSWORD)
        finally:
            self.tear_down()

    def test_invalid_login(self):
        login = 'Invalidy'
        password = '123456'

        try:
            self.set_up()
            self.input_login_form(login)
            self.input_password_form(password)
            self.click_button()

            assert self.wait_for_status_message(self.ERROR_WRONG_CREDENTIALS)
        finally:
            self.tear_down()

    def test_empty_login(self):
        login = ''
        password = '123456'

        try:
            self.set_up()
            self.input_login_form(login)
            self.input_password_form(password)
            self.click_button()

            assert self.wait_for_status_message(self.ERROR_SHORT_LOGIN)
        finally:
            self.tear_down()
