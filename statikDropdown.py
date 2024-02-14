
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait #ilgili driverı bekleten yapı
from selenium.webdriver.support import expected_conditions as ec #beklenen koşullar
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://tomspizzeria.b4a.app/")
driver.maximize_window()
dropdown = driver.find_element(By.ID,"odeme-tipi")
odeme = Select(dropdown)
odeme_tipleri = odeme.options #web element listesi, her bir option tagi,açılır listenin her bir elemanını listeye koyar

for tip in odeme_tipleri:
    print(tip.text)

sleep(2)
odeme.select_by_visible_text("Kredi Kartı") #textini verdiğim opsiyonu seçecek
sleep(2)
odeme.select_by_index(3) #indexini verdiğim opsiyonu seçecek
sleep(2)
#first_selecetion_options() birden fazla secenek varsa ilkini seçer
