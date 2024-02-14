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

driver.implicitly_wait(30)
driver.get("http://tomspizzeria.herokuapp.com/yeni-sekme.html")
facebook = driver.find_element(By.ID, "facebook").click()
twitter = driver.find_element(By.ID, "twitter").click()
instagram = driver.find_element(By.ID, "instagram").click()
sleep(2)

def sekme_degistir(baslik):
    for sayfa in driver.window_handles:
        driver.switch_to.window(sayfa)
        if baslik.lower() in driver.title.lower():
            break


sekme_degistir("facebook")
print("facebook: "+driver.title)

sekme_degistir("twitter")
print("twitter: "+driver.title)

sekme_degistir("instagram")
print("instagram: "+driver.title)

sekme_degistir("selenium")
print("anasayfa: "+driver.title)
