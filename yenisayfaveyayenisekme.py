from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait #ilgili driverı bekleten yapı
from selenium.webdriver.support import expected_conditions as ec #beklenen koşullar
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.apple.com")
driver.switch_to.new_window("tab") # yeni sekme açar
driver.get("https://www.tesla.com") #açtığı yeni sekmede bu linki açar

driver.switch_to.new_window("window") # yeni pencere açar