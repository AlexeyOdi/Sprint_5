import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators
import pytest
from tests.conftest import *
import random
import urls

@pytest.mark.usefixtures("get_driver")
class TestClass:

    def test_registation(self):

        self.driver.get(urls.url)
        self.driver.find_element(By.XPATH, locators.personal_account).click()
        self.driver.find_element(By.XPATH, locators.registration_page).click()
        self.driver.find_element(By.XPATH, locators.name_imput).send_keys("Alex")
        random_number = random.randint(10, 999999)
        self.driver.find_element(By.XPATH, locators.email_input_login).send_keys("Alex" + str(random_number) + "@mail.com")
        self.driver.find_element(By.XPATH, locators.password_input_login).send_keys("Alexalex")
        self.driver.find_element(By.XPATH, locators.registration_button).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.registration_page)))
        assert self.driver.current_url == urls.login_page

    def test_registration_incorrect_password(self):

        self.driver.get(urls.url)
        self.driver.find_element(By.XPATH, locators.personal_account).click()
        self.driver.find_element(By.XPATH, locators.registration_page).click()
        self.driver.find_element(By.XPATH, locators.name_imput).send_keys("Alex")
        self.driver.find_element(By.XPATH, locators.email_input_login).send_keys("Alex@mail.com")
        self.driver.find_element(By.XPATH, locators.password_input_login).send_keys("Alex")
        self.driver.find_element(By.XPATH, locators.registration_button).click()
        assert self.driver.find_element(By.XPATH, locators.uncorrect_password_msg).text == "Некорректный пароль"