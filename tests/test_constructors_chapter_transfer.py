from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time

######################### test_sause

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]').click()
element = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]')
assert "tab_tab_type_current__2BEPc" in element.get_attribute('class')



driver.quit()

######################### test bun

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]').click()
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[1]').click()
element = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[1]')
assert "tab_tab_type_current__2BEPc" in element.get_attribute('class')

driver.quit()

######################### test toppings

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3]').click()
element = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3]')
assert "tab_tab_type_current__2BEPc" in element.get_attribute('class')

driver.quit()

