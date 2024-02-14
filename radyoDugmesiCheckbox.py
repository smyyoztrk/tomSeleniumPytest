from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait #ilgili driverı bekleten yapı
from selenium.webdriver.support import expected_conditions as ec #beklenen koşullar
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://tomspizzeria.b4a.app/")
driver.maximize_window()
orta_boy = driver.find_element(By.CSS_SELECTOR,"input[value='Orta']")
zeytin = driver.find_element(By.CSS_SELECTOR,"input[value='zeytin']")
yesilbiber = driver.find_element(By.CSS_SELECTOR,"input[value='yesil biber']")
print(orta_boy.is_selected())
print(zeytin.is_selected())
print(yesilbiber.is_selected())
sleep(2)
orta_boy.click()
sleep(2)
zeytin.click()
sleep(2)
yesilbiber.click()
sleep(2)
print(orta_boy.is_selected())
print(zeytin.is_selected())
print(yesilbiber.is_selected())
