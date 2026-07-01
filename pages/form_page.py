from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class FormPage:

    def __init__(self, driver):
        self.driver = driver

    FULL_NAME_LOCATOR = (By.ID, "userName")
    RESULT_LOCATOR = (By.ID, "output")
    EMAIL_FIELD_LOCATOR = (By.ID, "userEmail")
    EMAIL_LOCATOR = (By.CSS_SELECTOR, "input[type='email']")
    CURRENT_ADDRESS_LOCATOR = (By.ID, "currentAddress")
    PERMANENT_ADDRESS_LOCATOR = (By.ID, "permanentAddress")
    SUBMIT_BUTTON_LOCATOR = (By.ID, "submit")

    URL = 'https://qa-guru.github.io/one-page-form/text-box.html'

    def open(self):
        self.driver.get(self.URL)

    def input_full_name(self, name):
        full_name_field = self.driver.find_element(*self.FULL_NAME_LOCATOR)
        full_name_field.send_keys(name)

    def input_email(self, email):
        email_field = self.driver.find_element(*self.EMAIL_FIELD_LOCATOR)
        email_field.send_keys(email)

    def input_current_address(self, address):
        current_address_field = self.driver.find_element(*self.CURRENT_ADDRESS_LOCATOR)
        current_address_field.send_keys(address)

    def input_permanent_address(self, address):
        permanent_address_field = self.driver.find_element(*self.PERMANENT_ADDRESS_LOCATOR)
        permanent_address_field.send_keys(address)

    def click_button(self):
        submit_button = self.driver.find_element(*self.SUBMIT_BUTTON_LOCATOR)
        submit_button.click()

    def get_email_validation_message(self):
        email_field = self.driver.find_element(*self.EMAIL_LOCATOR)
        return self.driver.execute_script(
            "return arguments[0].validationMessage",
            email_field
        )

    def get_result_box(self):
        return WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(self.RESULT_LOCATOR)
        )
