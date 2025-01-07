from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button').click()
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys("Alex@mail.com")
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys("Alexalex")
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()
driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a').click()
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div/main/div/div")))
assert driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile"


driver.quit()