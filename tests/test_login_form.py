import pytest
from pages.login_form_page import LoginFormPage


class TestLoginForm:

    @pytest.mark.parametrize("login, password, expected_error", [
        ('example', '1', 'Password must be at least 6 characters'),
        ('example', '', 'Password is required (minimum 6 characters'),
        ('Invalidy', '123456', 'Wrong login or password'),
        ('', '123456', 'Login is required (minimum 3 characters)')
    ])
    def test_login_error_messages(self, driver, login, password, expected_error):
        page = LoginFormPage(driver)
        page.open()

        page.input_login_form(login)
        page.input_password_form(password)
        page.click_button()

        assert page.wait_for_status_message(expected_error)
