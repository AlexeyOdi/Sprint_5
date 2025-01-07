from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time

## test_login_main_page

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button').click()
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys("Alex@mail.com")
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys("Alexalex")
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()
driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a').click()
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div/main/div/div")))
element = driver.find_element(By.XPATH, '//div/main/div/div/div/ul/li[2]/div/div/input')
assert element.get_attribute("value") == "alex@mail.com"

driver.quit()

## test_login_personal_cab

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

driver.find_element(By.XPATH, '//*/div/header/nav/a').click()
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Auth_link__1fOlj")))
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys("Alex@mail.com")
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys("Alexalex")
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()
driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a').click()
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div/main/div/div")))
element = driver.find_element(By.XPATH, '//div/main/div/div/div/ul/li[2]/div/div/input')
assert element.get_attribute("value") == "alex@mail.com"

driver.quit()

## test_login_from_reg_form

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

driver.find_element(By.XPATH, '//*/div/header/nav/a').click()
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Auth_link__1fOlj")))

driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p[1]/a').click()
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p/a').click()
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys("Alex@mail.com")
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys("Alexalex")
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()
driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a').click()
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div/main/div/div")))
element = driver.find_element(By.XPATH, '//div/main/div/div/div/ul/li[2]/div/div/input')
assert element.get_attribute("value") == "alex@mail.com"

time.sleep(2)
driver.quit()

## test_login_from_recover_password_form

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button').click()
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p[2]/a').click()
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p/a').click()
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys("Alex@mail.com")
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys("Alexalex")
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()
driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a').click()
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div/main/div/div")))
element = driver.find_element(By.XPATH, '//div/main/div/div/div/ul/li[2]/div/div/input')
assert element.get_attribute("value") == "alex@mail.com"

driver.quit()

