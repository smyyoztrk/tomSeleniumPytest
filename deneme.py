from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait #ilgili driverı bekleten yapı
from selenium.webdriver.support import expected_conditions as ec #beklenen koşullar
from selenium.webdriver.common.action_chains import ActionChains
import pytest
def imdb():
    driver = webdriver.Chrome()
    driver.get("https://www.imdb.com/")
    driver.maximize_window()
    driver.find_element(By.ID,"imdbHeader-navDrawerOpen").click()
    sleep(2)
    driver.find_element(By.XPATH,"//span[text()='Top 250 Movies']").click()
    sleep(3)
    film_isimleri = driver.find_elements(By.XPATH,"//div[@class='ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-43986a27-9 gaoUku cli-title']/a")
    sleep(2)
    for i in range(20):
        print(film_isimleri[i].text)

    
    driver.quit()
def sauce(username,password):
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    usernameInput = driver.find_element(By.ID,"user-name").send_keys(username)
    sleep(2)
    passwordInput = driver.find_element(By.ID,"password").send_keys(password)
    sleep(2)
    loginButton = driver.find_element(By.ID,"login-button").click()
    sleep(2)
    #mesaj = driver.find_element(By.XPATH,"//div[@class='error-message-container error']/h3").text
    addToCard = driver.find_elements(By.XPATH,"//div[@class='pricebar']/button")
    #print(f"add to car sayısı:{len(addToCard)}")
    sleep(1)
    # for i in addToCard:
    
    #     i.click()
    
    print(addToCard[0].text )


#     return mesaj
#     # print(mesaj)

# mesaj = sauce("locked_out_user","secret_sauce")  

# if "Epic sadface: Sorry, this user has been locked out." == mesaj:

#     print("test sonucu: True")
# else:
#     print("HATA")

sauce("standard_user","secret_sauce")

