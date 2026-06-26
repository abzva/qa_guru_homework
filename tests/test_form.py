from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestSuite:
    FULL_NAME_LOCATOR = (By.ID, "userName")
    RESULT_LOCATOR = (By.ID, "output")
    EMAIL_FIELD_LOCATOR = (By.ID, "userEmail")
    EMAIL_LOCATOR = (By.CSS_SELECTOR, "input[type='email']")
    CURRENT_ADDRESS_LOCATOR = (By.ID, "currentAddress")
    PERMANENT_ADDRESS_LOCATOR = (By.ID, "permanentAddress")
    SUBMIT_BUTTON_LOCATOR = (By.ID, "submit")

    def set_up(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def tear_down(self):
        self.driver.quit()

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

    def test_positive_email(self):
        name = 'Иван Иванов'
        email = 'ivan@example.com'

        try:
            self.set_up()
            self.input_full_name(name)
            self.input_email(email)
            self.click_button()
            result_box = self.get_result_box()

            assert name in result_box.text
            print("Тест успешно пройден!")

        finally:
            self.tear_down()

    def test_negative_no_at(self):
        name = 'Иван Иванов'
        email = 'ivanexample.com'

        try:
            self.set_up()
            self.input_full_name(name)
            self.input_email(email)
            self.click_button()
            validation_message = self.get_email_validation_message()

            assert 'Адрес электронной почты должен содержать символ "@". В адресе "ivanexample.com" отсутствует символ "@".' in validation_message
            print("Тест успешно пройден!")

        finally:
            self.tear_down()

    def test_negative_empty_email(self):
        name = 'Иван Иванов'
        email = ''

        try:
            self.set_up()
            self.input_full_name(name)
            self.input_email(email)
            self.click_button()
            result_box = self.driver.find_elements(*self.RESULT_LOCATOR)

            assert len(result_box) == 0, "БАГ: форма отправилась с пустым email!"
            print("Тест успешно пройден!")

        finally:
            self.tear_down()

    def test_negative_long_email(self):
        name = 'Иван Иванов'
        email = 'testivanivanovveryverutestivanivantestivanivanovveryverutestivanivanovveryverutestivanivanovveryverutestivanivanovveryveruovveryveru@google.com'

        try:
            self.set_up()
            self.input_full_name(name)
            self.input_email(email)
            self.click_button()
            result_box = self.driver.find_elements(*self.RESULT_LOCATOR)

            assert len(result_box) == 0, "БАГ: форма приняла слишком длинный email!"
            print("Тест успешно пройден!")

        finally:
            self.tear_down()

    def test_negative_special_chars_before_at(self):
        name = 'Иван Иванов'
        email = 'testivaniv№@google.com'

        try:
            self.set_up()
            self.input_full_name(name)
            self.input_email(email)
            self.click_button()
            validation_message = self.get_email_validation_message()

            assert 'Часть адреса до символа "@" не должна содержать символ "№".' in validation_message
            print("Тест успешно пройден!")

        finally:
            self.tear_down()

    def test_negative_special_chars_after_at(self):
        name = 'Иван Иванов'
        email = 'testivaniv@goo№gle.com'

        try:
            self.set_up()
            self.input_full_name(name)
            self.input_email(email)
            self.click_button()
            validation_message = self.get_email_validation_message()

            assert 'Часть адреса после символа "@" не должна содержать символ "№".' in validation_message
            print("Тест успешно пройден!")

        finally:
            self.tear_down()

    def test_sql_injection_in_email(self):
        name = 'Иван Иванов'
        email = "' OR '1'='1"

        try:
            self.set_up()
            self.input_full_name(name)
            self.input_email(email)
            self.click_button()
            result_box = self.driver.find_elements(*self.RESULT_LOCATOR)

            assert len(result_box) == 0, "БАГ: форма приняла SQL-инъекцию!"
            print("Тест успешно пройден!")

        finally:
            self.tear_down()

    def test_positive_current_address(self):
        name = 'Иван Иванов'
        email = 'ivan@example.com'
        current_address = 'г. Санкт-Петербург, Невский пр-кт'

        try:
            self.set_up()
            self.input_full_name(name)
            self.input_email(email)
            self.input_current_address(current_address)
            self.click_button()
            result_box = self.get_result_box()

            assert current_address in result_box.text
            print("Тест успешно пройден!")

        finally:
            self.tear_down()

    def test_positive_permanent_address(self):
        name = 'Иван Иванов'
        email = 'ivan@example.com'
        permanent_address = 'г. Санкт-Петербург, Московский пр-кт'

        try:
            self.set_up()
            self.input_full_name(name)
            self.input_email(email)
            self.input_permanent_address(permanent_address)
            self.click_button()
            result_box = self.get_result_box()

            assert permanent_address in result_box.text
            print("Тест успешно пройден!")

        finally:
            self.tear_down()
