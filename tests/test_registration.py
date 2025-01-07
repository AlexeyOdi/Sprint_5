from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time

## test_registration

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

driver.find_element(By.XPATH, '//*/div/header/nav/a').click()
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Auth_link__1fOlj")))

driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p[1]/a').click()
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys("Alex")
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys("Alex@mail.com")
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input').send_keys("Alexalex")
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()

assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

driver.quit()

## test_registration_incorrect_password

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

driver.find_element(By.XPATH, '//*/div/header/nav/a').click()
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Auth_link__1fOlj")))

driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p[1]/a').click()
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys("Alex")
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys("Alex@mail.com")
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input').send_keys("Alex")
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()

assert driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/p').text == "Некорректный пароль"

driver.quit()