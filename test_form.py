import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_positive_email():
    # 1. Запуск браузера Chrome
    driver = webdriver.Chrome()

    try:
        # 2. Открытие страницы
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(5)  # Пауза, чтобы визуально заметить открытие

        # 3. Поиск элементов и заполнение полей
        # Находим поле Full Name по его ID и вводим текст
        full_name_field = driver.find_element(By.ID, "userName")
        full_name_field.send_keys("Иван Иванов")

        # Находим поле Email по его ID и вводим текст
        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys("ivan@example.com")

        # Находим кнопку Submit по ее ID и кликаем
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # 4. Проверка результата
        time.sleep(5)  # Пауза, чтобы увидеть результат отправки

        # Находим блок с отправленными данными
        result_box = driver.find_element(By.ID, "output")

        # Проверяем, что в блоке результата появился введенный текст
        assert "Иван Иванов" in result_box.text
        print("Тест успешно пройден!")

    finally:
        # 5. Закрытие браузера в любом случае
        driver.quit()

def test_negative_no_at():
    # Негативный тест на проверку отсутствия @
    # 1. Запуск браузера Chrome
    driver = webdriver.Chrome()

    try:
        # 2. Открытие страницы
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(5)  # Пауза, чтобы визуально заметить открытие

        # 3. Поиск элементов и заполнение полей
        # Находим поле Full Name по его ID и вводим текст
        full_name_field = driver.find_element(By.ID, "userName")
        full_name_field.send_keys("Иван Иванов")

        # Находим поле Email по его ID и вводим неверный email
        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys("ivanexample.com")

        # Находим кнопку Submit по ее ID и кликаем
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # 4. Проверка результата
        time.sleep(5)  # Пауза, чтобы увидеть результат отправки

        # Получаем текст подсказки
        email_field = driver.find_element(By.CSS_SELECTOR, "input[type='email']")
        validation_message = driver.execute_script("return arguments[0].validationMessage", email_field)

        # Проверяем текст
        assert 'Адрес электронной почты должен содержать символ "@". В адресе "ivanexample.com" отсутствует символ "@".' in validation_message
        print("Тест успешно пройден!")

    finally:
        # 5. Закрытие браузера в любом случае
        driver.quit()

def test_negative_empty_email():
    # Негативный тест на пустой email
    # 1. Запуск браузера Chrome
    driver = webdriver.Chrome()

    try:
        # 2. Открытие страницы
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(5)  # Пауза, чтобы визуально заметить открытие

        # 3. Поиск элементов и заполнение полей
        # Находим поле Full Name по его ID и вводим текст
        full_name_field = driver.find_element(By.ID, "userName")
        full_name_field.send_keys("Иван Иванов")

        # Находим поле Email по его ID и вводим текст
        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys("")

        # Находим кнопку Submit по ее ID и кликаем
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # 4. Проверка результата
        time.sleep(5)  # Пауза, чтобы увидеть результат отправки

        # Находим блок с отправленными данными
        result_box = driver.find_elements(By.ID, "output")  # find_elements — возвращает список

        # Проверяем, что форма НЕ отправилась
        assert len(result_box) == 0, "БАГ: форма отправилась с пустым email!"
        print("Тест успешно пройден!")

    finally:
        # 5. Закрытие браузера в любом случае
        driver.quit()

def test_negative_long_email():
    # Негативный тест на длинный email
    # 1. Запуск браузера Chrome
    driver = webdriver.Chrome()

    try:
        # 2. Открытие страницы
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(5)  # Пауза, чтобы визуально заметить открытие

        # 3. Поиск элементов и заполнение полей
        # Находим поле Full Name по его ID и вводим текст
        full_name_field = driver.find_element(By.ID, "userName")
        full_name_field.send_keys("Иван Иванов")

        # Находим поле Email по его ID и вводим текст
        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys("testivanivanovveryverutestivanivantestivanivanovveryverutestivanivanovveryverutestivanivanovveryverutestivanivanovveryveruovveryveru@google.com")

        # Находим кнопку Submit по ее ID и кликаем
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # 4. Проверка результата
        time.sleep(5)  # Пауза, чтобы увидеть результат отправки

        # Находим блок с отправленными данными
        result_box = driver.find_elements(By.ID, "output")

        # Проверяем, что в блоке результата появился введенный текст
        assert len(result_box) == 0, "БАГ: форма приняла слишком длинный email!"
        print("Тест успешно пройден!")

    finally:
        # 5. Закрытие браузера в любом случае
        driver.quit()

def test_negative_special_chars_before_at():
    # Негативный тест спецсимволы в email до @
    # 1. Запуск браузера Chrome
    driver = webdriver.Chrome()

    try:
        # 2. Открытие страницы
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(5)  # Пауза, чтобы визуально заметить открытие

        # 3. Поиск элементов и заполнение полей
        # Находим поле Full Name по его ID и вводим текст
        full_name_field = driver.find_element(By.ID, "userName")
        full_name_field.send_keys("Иван Иванов")

        # Находим поле Email по его ID и вводим текст
        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys("testivaniv№@google.com")

        # Находим кнопку Submit по ее ID и кликаем
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # 4. Проверка результата
        time.sleep(5)  # Пауза, чтобы увидеть результат отправки

        # Получаем текст подсказки
        email_field = driver.find_element(By.CSS_SELECTOR, "input[type='email']")
        validation_message = driver.execute_script("return arguments[0].validationMessage", email_field)

        # Проверяем текст
        assert 'Часть адреса до символа "@" не должна содержать символ "№".' in validation_message
        print("Тест успешно пройден!")

    finally:
        # 5. Закрытие браузера в любом случае
        driver.quit()

def test_negative_special_chars_after_at():
    # Негативный тест спецсимволы в email после @
    # 1. Запуск браузера Chrome
    driver = webdriver.Chrome()

    try:
        # 2. Открытие страницы
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(5)  # Пауза, чтобы визуально заметить открытие

        # 3. Поиск элементов и заполнение полей
        # Находим поле Full Name по его ID и вводим текст
        full_name_field = driver.find_element(By.ID, "userName")
        full_name_field.send_keys("Иван Иванов")

        # Находим поле Email по его ID и вводим текст
        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys("testivaniv@goo№gle.com")

        # Находим кнопку Submit по ее ID и кликаем
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # 4. Проверка результата
        time.sleep(5)  # Пауза, чтобы увидеть результат отправки

        # Получаем текст подсказки
        email_field = driver.find_element(By.CSS_SELECTOR, "input[type='email']")
        validation_message = driver.execute_script("return arguments[0].validationMessage", email_field)

        # Проверяем текст
        assert 'Часть адреса после символа "@" не должна содержать символ "№".' in validation_message
        print("Тест успешно пройден!")

    finally:
        # 5. Закрытие браузера в любом случае
        driver.quit()

def test_sql_injection_in_email():
    # Негативный тест SQL-инъекция в email
    # 1. Запуск браузера Chrome
    driver = webdriver.Chrome()

    try:
        # 2. Открытие страницы
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(5)

        # 3. Поиск элементов и заполнение полей
        full_name_field = driver.find_element(By.ID, "userName")
        full_name_field.send_keys("Иван Иванов")

        # Вводим SQL-инъекцию в поле email
        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys("' OR '1'='1")

        # Находим кнопку Submit и кликаем
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # 4. Проверка результата
        time.sleep(5)

        # Проверяем что форма НЕ отправилась
        result_box = driver.find_elements(By.ID, "output")
        assert len(result_box) == 0, "БАГ: форма приняла SQL-инъекцию!"
        print("Тест успешно пройден!")

    finally:
        # 5. Закрытие браузера в любом случае
        driver.quit()

def test_positive_current_address():
    # 1. Запуск браузера Chrome
    driver = webdriver.Chrome()

    try:
        # 2. Открытие страницы
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(5)  # Пауза, чтобы визуально заметить открытие

        # 3. Поиск элементов и заполнение полей
        # Находим поле Full Name по его ID и вводим текст
        full_name_field = driver.find_element(By.ID, "userName")
        full_name_field.send_keys("Иван Иванов")

        # Находим поле Email по его ID и вводим текст
        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys("ivan@example.com")

        # Находим поле current_address по ID и вводим текст
        current_address_field = driver.find_element(By.ID, "currentAddress")
        current_address_field.send_keys("г. Санкт-Петербург, Невский пр-кт")

        # Находим кнопку Submit по ее ID и кликаем
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # 4. Проверка результата
        time.sleep(5)  # Пауза, чтобы увидеть результат отправки

        # Находим блок с отправленными данными
        result_box = driver.find_element(By.ID, "output")

        # Проверяем, что в блоке результата появился введенный текст
        assert "г. Санкт-Петербург, Невский пр-кт" in result_box.text
        print("Тест успешно пройден!")

    finally:
        # 5. Закрытие браузера в любом случае
        driver.quit()

def test_positive_permanent_address():
    # 1. Запуск браузера Chrome
    driver = webdriver.Chrome()

    try:
        # 2. Открытие страницы
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(5)  # Пауза, чтобы визуально заметить открытие

        # 3. Поиск элементов и заполнение полей
        # Находим поле Full Name по его ID и вводим текст
        full_name_field = driver.find_element(By.ID, "userName")
        full_name_field.send_keys("Иван Иванов")

        # Находим поле Email по его ID и вводим текст
        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys("ivan@example.com")

        # Находим поле current_address по ID и вводим текст
        permanent_address_field = driver.find_element(By.ID, "permanentAddress")
        permanent_address_field.send_keys("г. Санкт-Петербург, Московский пр-кт")

        # Находим кнопку Submit по ее ID и кликаем
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # 4. Проверка результата
        time.sleep(5)  # Пауза, чтобы увидеть результат отправки

        # Находим блок с отправленными данными
        result_box = driver.find_element(By.ID, "output")

        # Проверяем, что в блоке результата появился введенный текст
        assert "г. Санкт-Петербург, Московский пр-кт" in result_box.text
        print("Тест успешно пройден!")

    finally:
        # 5. Закрытие браузера в любом случае
        driver.quit()



