from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time
import locators
import pytest
from conftest import *
import random

@pytest.mark.usefixtures("get_driver")
class TestClass:

    def test_registation(self):

        self.driver.get(locators.url)
        self.driver.find_element(By.XPATH, locators.personal_account).click()
        #WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Auth_link__1fOlj")))
        self.driver.find_element(By.XPATH, locators.registration_page).click()
        self.driver.find_element(By.XPATH, locators.name_imput).send_keys("Alex")
        random_number = random.randint(10, 999999)
        self.driver.find_element(By.XPATH, locators.email_input_reg).send_keys("Alex"+str(random_number)+"@mail.com")
        self.driver.find_element(By.XPATH, locators.password_input_reg).send_keys("Alexalex")
        self.driver.find_element(By.XPATH, locators.registration_button).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div/main/div/form")))
        assert self.driver.current_url == locators.login_page

    def test_registration_incorrect_password(self):

        self.driver.get(locators.url)
        self.driver.find_element(By.XPATH, locators.personal_account).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Auth_link__1fOlj")))
        self.driver.find_element(By.XPATH, locators.registration_page).click()
        self.driver.find_element(By.XPATH, locators.name_imput).send_keys("Alex")
        self.driver.find_element(By.XPATH, locators.email_input_reg).send_keys("Alex@mail.com")
        self.driver.find_element(By.XPATH, locators.password_input_reg).send_keys("Alex")
        self.driver.find_element(By.XPATH, locators.registration_button).click()
        assert self.driver.find_element(By.XPATH, locators.uncorrect_password_msg).text == "Некорректный пароль"