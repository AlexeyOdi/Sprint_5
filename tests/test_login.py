from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators
import pytest
from tests.conftest import *
import urls

@pytest.mark.usefixtures("get_driver")
class TestClass:

    def test_login_main_page(self):

        self.driver.get(urls.url)
        self.driver.find_element(By.XPATH, locators.login_button_on_main).click()
        self.driver.find_element(By.XPATH, locators.email_input_login).send_keys("Alex@mail.com")
        self.driver.find_element(By.XPATH, locators.password_input_login).send_keys("Alexalex")
        self.driver.find_element(By.XPATH, locators.login_button_on_login_page).click()
        self.driver.find_element(By.XPATH, locators.personal_account).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.profile_data_form_text)))
        assert self.driver.current_url == urls.account_page

    def test_login_personal_cab(self):

        self.driver.get(urls.url)
        self.driver.find_element(By.XPATH, locators.personal_account).click()
        self.driver.find_element(By.XPATH, locators.email_input_login).send_keys("Alex@mail.com")
        self.driver.find_element(By.XPATH, locators.password_input_login).send_keys("Alexalex")
        self.driver.find_element(By.XPATH, locators.login_button_on_login_page).click()
        self.driver.find_element(By.XPATH, locators.personal_account).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.profile_data_form_text)))
        assert self.driver.current_url == urls.account_page

    def test_login_from_reg_form(self):

        self.driver.get(urls.url)
        self.driver.find_element(By.XPATH, locators.personal_account).click()
        self.driver.find_element(By.XPATH, locators.registration_page).click()
        self.driver.find_element(By.XPATH, locators.login_button_on_reg_page).click()
        self.driver.find_element(By.XPATH, locators.email_input_login).send_keys("Alex@mail.com")
        self.driver.find_element(By.XPATH, locators.password_input_login).send_keys("Alexalex")
        self.driver.find_element(By.XPATH, locators.login_button_on_login_page).click()
        self.driver.find_element(By.XPATH, locators.personal_account).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locators.profile_data_form_text)))
        assert self.driver.current_url == urls.account_page

    def test_login_from_recover_password_form(self):

        self.driver.get(urls.url)
        self.driver.find_element(By.XPATH, locators.login_button_on_main).click()
        self.driver.find_element(By.XPATH, locators.password_recover_button).click()
        self.driver.find_element(By.XPATH, locators.login_button_on_reg_page).click()
        self.driver.find_element(By.XPATH, locators.email_input_login).send_keys("Alex@mail.com")
        self.driver.find_element(By.XPATH, locators.password_input_login).send_keys("Alexalex")
        self.driver.find_element(By.XPATH, locators.login_button_on_login_page).click()
        self.driver.find_element(By.XPATH, locators.personal_account).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locators.profile_data_form_text)))
        assert self.driver.current_url == urls.account_page

