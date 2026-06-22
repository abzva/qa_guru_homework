import os
import automation_practice_form_po

class AutomationPracticeFormTestSuite:

    def setup(self):
        self.automation_practice_form = automation_practice_form_po.AutomationPracticeFormPO("https://qa-guru.github.io/one-page-form/automation-practice-form.html")
        self.automation_practice_form.setup()
        self.tmp_file_name = self._create_tmp_file()

    def _create_tmp_file(self):
        file_path = os.path.abspath('test_file.jpg')
        with open(file_path, 'w') as file:
            file.write("Test")
        return file_path
    
    def test_form_positive01(self):
        self.automation_practice_form.fill_in_form(self.tmp_file_name, "Dmitry","Bugaev", "bugaev@example.com", "Male","1234567890",("1988", "4", "22"),("Maths", "English"), ("Sports", "Music"), "г. Санкт-Петербург, ул. Невский проспект, д 101", "NCR",  "Noida")
        self.automation_practice_form.assert_student_name('Dmitry', 'Bugaev')
        self.automation_practice_form.assert_email('bugaev@example.com')
        self.automation_practice_form.assert_result_is_visible()

    def test_form_positive02(self):
        self.automation_practice_form.fill_in_form(self.tmp_file_name, "Lena","Petrova", "petrovlen@example.com", "Female", "9876543210", ("1995", "7", "15"), ("Chemistry", "Physics"), ("Reading", "Music"), "г. Москва, ул. Арбат, д 25", "Uttar Pradesh", "Agra")
        self.automation_practice_form.assert_student_name('Lena', 'Petrova')
        self.automation_practice_form.assert_email('petrovlen@example.com')
        self.automation_practice_form.assert_result_is_visible()

    def tear_down(self):
        if os.path.exists(self.tmp_file_name):
            os.remove(self.tmp_file_name)
        self.automation_practice_form.tear_down()


test_suite = AutomationPracticeFormTestSuite()

try:
    test_suite.setup()
    test_suite.test_form_positive01()
finally:
    test_suite.tear_down()

try:
    test_suite.setup()
    test_suite.test_form_positive02()
finally:
    test_suite.tear_down()

