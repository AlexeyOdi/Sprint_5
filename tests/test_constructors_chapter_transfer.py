from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time
import locators
import pytest
from conftest import get_driver

@pytest.mark.usefixtures("get_driver")
class TestClass():

    def test_sause(self):

        self.driver.get(locators.url)
        self.driver.find_element(By.XPATH, locators.sause_chapter).click()
        element = self.driver.find_element(By.XPATH, locators.sause_chapter)
        assert "tab_tab_type_current__2BEPc" in element.get_attribute('class')

    def test_bun(self):

        self.driver.get(locators.url)
        self.driver.find_element(By.XPATH, locators.sause_chapter).click()
        self.driver.find_element(By.XPATH, locators.bun_chapter).click()
        element = self.driver.find_element(By.XPATH, locators.bun_chapter)
        assert "tab_tab_type_current__2BEPc" in element.get_attribute('class')

    def test_toppings(self):

        self.driver.get(locators.url)
        self.driver.find_element(By.XPATH, locators.topping_chapter).click()
        element = self.driver.find_element(By.XPATH, locators.topping_chapter)
        assert "tab_tab_type_current__2BEPc" in element.get_attribute('class')

