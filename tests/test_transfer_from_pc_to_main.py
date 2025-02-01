from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators
import pytest
from tests.conftest import *
import urls

@pytest.mark.usefixtures("get_driver")
class TestClass:

    def test_transfer_from_pa_to_main(self):

        self.driver.get(urls.url)
        self.driver.find_element(By.XPATH, locators.login_button_on_main).click()
        self.driver.find_element(By.XPATH, locators.email_input_login).send_keys("Alex@mail.com")
        self.driver.find_element(By.XPATH, locators.password_input_login).send_keys("Alexalex")
        self.driver.find_element(By.XPATH, locators.login_button_on_login_page).click()
        self.driver.find_element(By.XPATH, locators.logo).click()
        assert self.driver.current_url == urls.url



