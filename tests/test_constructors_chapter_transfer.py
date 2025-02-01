from selenium.webdriver.common.by import By
import locators
import pytest
from tests.conftest import get_driver
import urls

@pytest.mark.usefixtures("get_driver")
class TestClass():

    def test_sause(self):

        self.driver.get(urls.url)
        self.driver.find_element(By.XPATH, locators.sause_chapter).click()
        element = self.driver.find_element(By.XPATH, locators.sause_chapter)
        assert "tab_tab_type_current__2BEPc" in element.get_attribute('class')

    def test_bun(self):

        self.driver.get(urls.url)
        self.driver.find_element(By.XPATH, locators.sause_chapter).click()
        self.driver.find_element(By.XPATH, locators.bun_chapter).click()
        element = self.driver.find_element(By.XPATH, locators.bun_chapter)
        assert "tab_tab_type_current__2BEPc" in element.get_attribute('class')

    def test_toppings(self):

        self.driver.get(urls.url)
        self.driver.find_element(By.XPATH, locators.topping_chapter).click()
        element = self.driver.find_element(By.XPATH, locators.topping_chapter)
        assert "tab_tab_type_current__2BEPc" in element.get_attribute('class')

