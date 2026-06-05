import os
import random
import datetime

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestRegistrationForm:
    FIRST_NAME_INPUT = (By.ID, 'firstName')
    LAST_NAME_INPUT = (By.ID, 'lastName')
    EMAIL_INPUT = (By.ID, 'userEmail')
    GENDER = (By.ID, 'genterWrapper')
    MOBILE_INPUT = (By.ID, 'userNumber')
    DATE_OF_BIRTH = (By.ID, 'dateOfBirthInput')
    CALENDAR = (By.ID, 'datepickerDays')
    CALENDAR_MONTH = (By.CSS_SELECTOR, '.react-datepicker__month-select')
    CALENDAR_YEAR = (By.CSS_SELECTOR, '.react-datepicker__year-select')
    CALENDAR_DAY = (By.CSS_SELECTOR, '.react-datepicker__day')
    SUBJECTS_INPUT = (By.ID, 'subjectsInput')
    HOBBIES = (By.ID, 'hobbiesWrapper')
    PICTURE = (By.ID, 'uploadPicture')
    CURRENT_ADDRESS = (By.ID, 'currentAddress')
    STATE = (By.ID, 'state')
    CITY = (By.ID, 'city')
    SUBMIT_BUTTON = (By.ID, 'submit')
    RESULT_FORM = (By.ID, 'resultBody')
    POPUP_CLOSE = (By.CSS_SELECTOR, 'button[aria-label="Close"]')

    def set_up(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://qa-guru.github.io/one-page-form/automation-practice-form.html')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def tear_down(self):
        self.driver.quit()

    def input_first_name(self, first_name):
        input_name = self.driver.find_element(*self.FIRST_NAME_INPUT)
        input_name.send_keys(first_name)

    def input_last_name(self, last_name):
        input_name = self.driver.find_element(*self.LAST_NAME_INPUT)
        input_name.send_keys(last_name)

    def input_email(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def select_gender(self, value):
        checkbox = self.driver.find_element(By.CSS_SELECTOR, f'input[type="radio"][value="{value}"]')
        checkbox.click()

    def input_mobile_number(self, number):
        input_number = self.driver.find_element(*self.MOBILE_INPUT)
        input_number.send_keys(number)

    def select_date_of_birth(self, day, month, year):
        self.driver.find_element(*self.DATE_OF_BIRTH).click()
        Select(self.driver.find_element(*self.CALENDAR_MONTH)).select_by_visible_text(month)
        Select(self.driver.find_element(*self.CALENDAR_YEAR)).select_by_visible_text(str(year))
        self.driver.find_element(By.CSS_SELECTOR, f'[data-day="{day}"]').click()

    def select_subjects(self, *subjects):
        for subject in subjects:
            self.driver.find_element(*self.SUBJECTS_INPUT).send_keys(subject)
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'subjects-auto-complete__option'))
            ).click()

    def select_hobbies(self, *hobbies):
        for hobby in hobbies:
            self.driver.find_element(
                By.CSS_SELECTOR, f'#hobbiesWrapper input[value="{hobby}"]'
            ).click()

    def upload_picture(self, path):
        file_path = os.path.abspath(path)
        self.driver.find_element(*self.PICTURE).send_keys(file_path)

    def input_current_address(self, address):
        self.driver.find_element(*self.CURRENT_ADDRESS).send_keys(address)

    def select_option_by_text(self, trigger_locator, options_class, text):
        element = self.driver.find_element(*trigger_locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)
        element.click()
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, options_class))
        )
        options = self.driver.find_elements(By.CLASS_NAME, options_class)
        for option in options:
            if option.text == text:
                option.click()
                break

    def select_state(self, state):
        self.select_option_by_text(self.STATE, 'state-city-option', state)

    def select_city(self, city):
        self.select_option_by_text(self.CITY, 'state-city-option', city)

    def clear_first_name(self):
        self.driver.find_element(*self.FIRST_NAME_INPUT).clear()

    def click_button(self):
        element = self.driver.find_element(*self.SUBMIT_BUTTON)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)
        element.click()

    def get_result_text(self):
        return self.driver.find_element(*self.RESULT_FORM).text

    def close_popup(self):
        self.driver.find_element(*self.POPUP_CLOSE).click()

    def test_registration_with_required_fields(self):
        first_name = 'Gena'
        last_name = 'Litvin'
        gender = 'Female'
        mobile = str(random.randint(1000000000, 9999999999))

        try:
            self.set_up()
            self.close_popup()
            self.input_first_name(first_name)
            self.input_last_name(last_name)
            self.select_gender(gender)
            self.input_mobile_number(mobile)
            self.click_button()

            result = self.get_result_text()

            checks = {
                'first_name': first_name in result,
                'last_name': last_name in result,
                'gender': gender in result,
                'mobile': mobile in result,
            }

            failed = [key for key, value in checks.items() if not value]
            assert not failed, f'Не прошли проверки: {failed}'

        finally:
            self.tear_down()

    def test_registration_form_with_all_fields(self):
        first_name = 'Galina'
        last_name = 'Bondar'
        email = 'example@mail.com'
        gender = 'Female'
        mobile = str(random.randint(1000000000, 9999999999))
        day = 3
        month = 'November'
        year = '2000'
        date_of_birth = datetime.strptime(f'{day} {month} {year}', '%d %B %Y').strftime('%d %b %Y')
        subjects = 'Maths', 'English', 'Physics'
        hobbies = 'Sports', 'Reading'
        picture = 'file.pages'
        address = 'г. Санкт-Петербург Невский пр-кт'
        state = 'NCR'
        city = 'Delhi'

        try:
            self.set_up()
            self.close_popup()
            self.input_first_name(first_name)
            self.input_last_name(last_name)
            self.input_email(email)
            self.select_gender(gender)
            self.input_mobile_number(mobile)
            self.select_date_of_birth(day, month, year)
            self.select_subjects(*subjects)
            self.select_hobbies(*hobbies)
            self.upload_picture(f'resources/{picture}')
            self.input_current_address(address)
            self.select_state(state)
            self.select_city(city)

            self.click_button()

            result = self.get_result_text()

            checks = {
                'first_name': first_name in result,
                'last_name': last_name in result,
                'email': email in result,
                'gender': gender in result,
                'mobile': mobile in result,
                'date_of_birth': date_of_birth in result,
                'subjects': all(s in result for s in subjects),
                'picture': picture in result,
                'address': address in result,
                'state': state in result,
                'city': city in result,
            }

            failed = [key for key, value in checks.items() if not value]
            assert not failed, f'Не прошли проверки: {failed}'

        finally:
            self.tear_down()

    def test_clear_first_name_field(self):
        first_name = 'Gena'
        new_first_name = 'Mark'
        last_name = 'Litvin'
        gender = 'Female'
        mobile = str(random.randint(1000000000, 9999999999))

        try:
            self.set_up()
            self.close_popup()
            self.input_first_name(first_name)
            self.input_last_name(last_name)
            self.select_gender(gender)
            self.input_mobile_number(mobile)
            self.clear_first_name()
            self.input_first_name(new_first_name)
            self.click_button()

            result = self.get_result_text()

            checks = {
                'first_name': new_first_name in result,
                'last_name': last_name in result,
                'gender': gender in result,
                'mobile': mobile in result,
            }

            failed = [key for key, value in checks.items() if not value]
            assert not failed, f'Не прошли проверки: {failed}'

        finally:
            self.tear_down()
