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

def siparisVer():
    driver.find_element(By.ID,"siparis").click()

def mesajOku():
    return driver.find_element(By.ID,"mesaj").text

#müsteri ismi
#Müşteri ismi girmediniz
siparisVer()
mesaj = mesajOku()
assert mesaj == "Müşteri ismi girmediniz"



#pizza boyu
#Pizza boyu seçmediniz

musteri_ismi = driver.find_element(By.ID,"musteri-adi")
musteri_ismi.send_keys("ALİ KOÇ")
siparisVer()
mesaj = mesajOku()
assert mesaj == mesajOku()



#ödeme şekli
#Ödeme tipi seçmediniz
driver.find_element(By.CSS_SELECTOR,"input[value='Küçük']").click()
siparisVer()
mesaj = mesajOku()
assert mesaj == "Ödeme tipi seçmediniz"



#Siparişiniz alındı
acilir_liste = driver.find_element(By.ID,"odeme-tipi")
odeme = Select(acilir_liste)
odeme.select_by_index(2)
siparisVer()
mesaj = mesajOku()
assert mesaj == "Siparişiniz alındı"
sleep(3)

# Müşteri ismi: ALİ KOÇ
musteri = driver.find_element(By.ID,"musteri").text
assert musteri == "Müşteri ismi: ALİ KOÇ"
# Pizza boyu: Küçük
pizzaBoyu = driver.find_element(By.ID,"pizzaboyu").text
assert pizzaBoyu == "Pizza boyu: Küçük"
# Pizza üstü:
pizzaUstu = driver.find_element(By.ID,"pizzaustu").text
assert pizzaUstu == "Pizza üstü:"
# Ödeme tipi: Kredi Kartı
odeme_tipi = driver.find_element(By.ID,"odeme").text
assert odeme_tipi == "Ödeme tipi: Kredi Kartı"
# Tutar: 10 TL
tutar = driver.find_element(By.ID,"tutar").text
assert tutar == "Tutar: 10 TL"
