from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from seleniumpagefactory.Pagefactory import PageFactory


class LoginFormPage(PageFactory):

    def __init__(self, driver):
        self.driver = driver
        self.locators = {
            "login_input": ("ID", 'login-input'),
            "password_input": ("ID", 'password-input'),
            "submit_button": ("ID", 'submit-button')
        }

    STATUS_MESSAGE_LOCATOR = (By.ID, 'error-message')

    URL = 'https://qa-guru.github.io/one-page-form/login.html'

    def open(self):
        self.driver.get(self.URL)

    def input_login_form(self, login):
        self.login_input.send_keys(login)

    def input_password_form(self, password):
        self.password_input.send_keys(password)

    def click_button(self):
        self.submit_button.click()

    def wait_for_status_message(self, text):
        return WebDriverWait(
            self.driver,
            timeout=5,
            poll_frequency=0.5
        ).until(
            ec.text_to_be_present_in_element(
                self.STATUS_MESSAGE_LOCATOR,
                text
            )
        )
