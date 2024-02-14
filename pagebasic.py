from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait #ilgili driverı bekleten yapı
from selenium.webdriver.support import expected_conditions as ec #beklenen koşullar
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pytest
import json
import openpyxl

class classAramaSayfasi:
    def __init__(self,driver):
        self.driver= driver
    # def webdriver_wait(self,sure,element):
    #     element=WebDriverWait(self.driver,sure).until(ec.visibility_of_element_located((By.CSS_SELECTOR,element)))
    #     return element
    ARAMA_KUTUSU_ID_WEBELEMENT = "small-searchterms"
    UYARI_MESAJI_CSS = "div[class='search-results']"
    DIAMOND_TEXT_CSS = "div[class='product-item'] h2>a"
    def arama_yap(self,kelime):
        arama_kutusu = self.driver.find_element(By.ID,self.ARAMA_KUTUSU_ID_WEBELEMENT)
        arama_kutusu.send_keys(kelime)
        arama_kutusu.send_keys(Keys.ENTER)
    def arama_uyari_mesajini_ver(self):
        uyari_mesaji = self.driver.find_element(By.CSS_SELECTOR,self.UYARI_MESAJI_CSS).text
        return uyari_mesaji
    def webelement_textini_ver(self,webelement):
        metin_listesi = self.driver.find_elements(By.CSS_SELECTOR,webelement)
        return metin_listesi

        