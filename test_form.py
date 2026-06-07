import time
from selenium import webdriver
from selenium.webdriver.common.by import By

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
        time.sleep(5)

    def tear_down(self):
        self.driver.quit()

    def get_full_name(self,name):
        full_name_field = self.driver.find_element(*self.FULL_NAME_LOCATOR)
        full_name_field.send_keys(name)

    def get_email(self,email):
        email_field = self.driver.find_element(*self.EMAIL_FIELD_LOCATOR)
        email_field.send_keys(email)

    def get_current_address(self,address):
        current_address_field = self.driver.find_element(*self.CURRENT_ADDRESS_LOCATOR)
        current_address_field.send_keys(address)

    def get_permanent_address(self,address):
        permanent_address_field = self.driver.find_element(*self.PERMANENT_ADDRESS_LOCATOR)
        permanent_address_field.send_keys(address)

    def clik_button(self):
        submit_button = self.driver.find_element(*self.SUBMIT_BUTTON_LOCATOR)
        submit_button.click()
        time.sleep(5)



    def test_positive_email(self):

        try:
            self.set_up()
            self.get_full_name("Иван Иванов")
            self.get_email("ivan@example.com")
            self.clik_button()
            result_box = self.driver.find_element(*self.RESULT_LOCATOR)

            assert "Иван Иванов" in result_box.text
            print("Тест успешно пройден!")

        finally:
            self.tear_down()

    def test_negative_no_at(self):

        try:
            self.set_up()
            self.get_full_name("Иван Иванов")
            self.get_email("ivanexample.com")
            self. clik_button()
            email_field = self.driver.find_element(*self.EMAIL_LOCATOR)
            validation_message = self.driver.execute_script("return arguments[0].validationMessage", email_field)

            assert 'Адрес электронной почты должен содержать символ "@". В адресе "ivanexample.com" отсутствует символ "@".' in validation_message
            print("Тест успешно пройден!")

        finally:
            self.tear_down()

    def test_negative_empty_email(self):

        try:
            self.set_up()
            self.get_full_name("Иван Иванов")
            self. get_email("")
            self. clik_button()
            result_box = self.driver.find_elements(*self.RESULT_LOCATOR)

            assert len(result_box) == 0, "БАГ: форма отправилась с пустым email!"
            print("Тест успешно пройден!")

        finally:
            self.tear_down()

    def test_negative_long_email(self):

        try:
            self.set_up()
            self.get_full_name("Иван Иванов")
            self.get_email("testivanivanovveryverutestivanivantestivanivanovveryverutestivanivanovveryverutestivanivanovveryverutestivanivanovveryveruovveryveru@google.com")
            self.clik_button()
            result_box = self.driver.find_elements(*self.RESULT_LOCATOR)

            assert len(result_box) == 0, "БАГ: форма приняла слишком длинный email!"
            print("Тест успешно пройден!")

        finally:
            self.tear_down()

    def test_negative_special_chars_before_at(self):

        try:
            self.set_up()
            self.get_full_name("Иван Иванов")
            self.get_email("testivaniv№@google.com")
            self.clik_button()
            email_field = self.driver.find_element(*self.EMAIL_LOCATOR)
            validation_message = self.driver.execute_script("return arguments[0].validationMessage", email_field)

            assert 'Часть адреса до символа "@" не должна содержать символ "№".' in validation_message
            print("Тест успешно пройден!")

        finally:
            self.tear_down()

    def test_negative_special_chars_after_at(self):

        try:
            self.set_up()
            self.get_full_name("Иван Иванов")
            self.get_email("testivaniv@goo№gle.com")
            self.clik_button()
            email_field = self.driver.find_element(*self.EMAIL_LOCATOR)
            validation_message = self.driver.execute_script("return arguments[0].validationMessage", email_field)

            assert 'Часть адреса после символа "@" не должна содержать символ "№".' in validation_message
            print("Тест успешно пройден!")

        finally:
            self.tear_down()

    def test_sql_injection_in_email(self):

        try:
            self.set_up()
            self.get_full_name("Иван Иванов")
            self.get_email("' OR '1'='1")
            self.clik_button()
            result_box = self.driver.find_elements(*self.RESULT_LOCATOR)

            assert len(result_box) == 0, "БАГ: форма приняла SQL-инъекцию!"
            print("Тест успешно пройден!")

        finally:
            self.tear_down()

    def test_positive_current_address(self):

        try:
            self.set_up()
            self.get_full_name("Иван Иванов")
            self.get_email("ivan@example.com")
            self.get_current_address("г. Санкт-Петербург, Невский пр-кт")
            self.clik_button()
            result_box = self.driver.find_element(*self.RESULT_LOCATOR)

            assert "г. Санкт-Петербург, Невский пр-кт" in result_box.text
            print("Тест успешно пройден!")

        finally:
            self.tear_down()

    def test_positive_permanent_address(self):

        try:
            self.set_up()
            self.get_full_name("Иван Иванов")
            self.get_email("ivan@example.com")
            self.get_permanent_address("г. Санкт-Петербург, Московский пр-кт")
            self.clik_button()
            result_box = self.driver.find_element(*self.RESULT_LOCATOR)

            assert "г. Санкт-Петербург, Московский пр-кт" in result_box.text
            print("Тест успешно пройден!")

        finally:
            self.tear_down()
