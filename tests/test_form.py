from pages.form_page import FormPage


class TestSuite:

    def test_positive_email(self, driver):
        page = FormPage(driver)
        page.open()

        name = 'Иван Иванов'
        email = 'ivan@example.com'

        page.input_full_name(name)
        page.input_email(email)
        page.click_button()
        result_box = page.get_result_box()

        assert name in result_box.text

    def test_negative_no_at(self, driver):
        page = FormPage(driver)
        page.open()

        name = 'Иван Иванов'
        email = 'ivanexample.com'

        page.input_full_name(name)
        page.input_email(email)
        page.click_button()
        validation_message = page.get_email_validation_message()

        assert 'Адрес электронной почты должен содержать символ "@". В адресе "ivanexample.com" отсутствует символ "@".' in validation_message

    def test_negative_empty_email(self, driver):
        page = FormPage(driver)
        page.open()

        name = 'Иван Иванов'
        email = ''

        page.input_full_name(name)
        page.input_email(email)
        page.click_button()
        result_box = page.driver.find_elements(*page.RESULT_LOCATOR)

        assert len(result_box) == 0, "БАГ: форма отправилась с пустым email!"

    def test_negative_long_email(self, driver):
        page = FormPage(driver)
        page.open()

        name = 'Иван Иванов'
        email = 'testivanivanovveryverutestivanivantestivanivanovveryverutestivanivanovveryverutestivanivanovveryverutestivanivanovveryveruovveryveru@google.com'

        page.input_full_name(name)
        page.input_email(email)
        page.click_button()
        result_box = page.driver.find_elements(*page.RESULT_LOCATOR)

        assert len(result_box) == 0, "БАГ: форма приняла слишком длинный email!"

    def test_negative_special_chars_before_at(self, driver):
        page = FormPage(driver)
        page.open()

        name = 'Иван Иванов'
        email = 'testivaniv№@google.com'

        page.input_full_name(name)
        page.input_email(email)
        page.click_button()
        validation_message = page.get_email_validation_message()

        assert 'Часть адреса до символа "@" не должна содержать символ "№".' in validation_message

    def test_negative_special_chars_after_at(self, driver):
        page = FormPage(driver)
        page.open()

        name = 'Иван Иванов'
        email = 'testivaniv@goo№gle.com'

        page.input_full_name(name)
        page.input_email(email)
        page.click_button()
        validation_message = page.get_email_validation_message()

        assert 'Часть адреса после символа "@" не должна содержать символ "№".' in validation_message, "БАГ: нет сообщения"

    def test_sql_injection_in_email(self, driver):
        page = FormPage(driver)
        page.open()

        name = 'Иван Иванов'
        email = "' OR '1'='1"

        page.input_full_name(name)
        page.input_email(email)
        page.click_button()
        result_box = page.driver.find_elements(*page.RESULT_LOCATOR)

        assert len(result_box) == 0, "БАГ: форма приняла SQL-инъекцию!"

    def test_positive_current_address(self, driver):
        page = FormPage(driver)
        page.open()

        name = 'Иван Иванов'
        email = 'ivan@example.com'
        current_address = 'г. Санкт-Петербург, Невский пр-кт'

        page.input_full_name(name)
        page.input_email(email)
        page.input_current_address(current_address)
        page.click_button()
        result_box = page.get_result_box()

        assert current_address in result_box.text

    def test_positive_permanent_address(self, driver):
        page = FormPage(driver)
        page.open()

        name = 'Иван Иванов'
        email = 'ivan@example.com'
        permanent_address = 'г. Санкт-Петербург, Московский пр-кт'

        page.input_full_name(name)
        page.input_email(email)
        page.input_permanent_address(permanent_address)
        page.click_button()
        result_box = page.get_result_box()

        assert permanent_address in result_box.text
