from pages.login_form_page import LoginFormPage


class TestLoginForm:

    def test_login_with_short_password(self, driver):
        page = LoginFormPage(driver)
        page.open()

        login = 'example'
        password = '1'

        page.input_login_form(login)
        page.input_password_form(password)
        page.click_button()

        assert page.wait_for_status_message(page.error_short_password)

    def test_empty_password(self, driver):
        page = LoginFormPage(driver)
        page.open()

        login = 'example'
        password = ''

        page.input_login_form(login)
        page.input_password_form(password)
        page.click_button()

        assert page.wait_for_status_message(page.error_password_required)

    def test_invalid_login(self, driver):
        page = LoginFormPage(driver)
        page.open()
        login = 'Invalidy'
        password = '123456'

        page.input_login_form(login)
        page.input_password_form(password)
        page.click_button()

        assert page.wait_for_status_message(page.error_wrong_credentials)

    def test_empty_login(self, driver):
        page = LoginFormPage(driver)
        page.open()
        login = ''
        password = '123456'

        page.input_login_form(login)
        page.input_password_form(password)
        page.click_button()

        assert page.wait_for_status_message(page.error_short_login)
