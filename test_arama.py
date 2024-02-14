from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait #ilgili driverı bekleten yapı
from selenium.webdriver.support import expected_conditions as ec #beklenen koşullar
from selenium.webdriver.common.action_chains import ActionChains
import pytest
import json
import openpyxl
from pagebasic import classAramaSayfasi
from data import classData

class TestArama:
    def setup_method(self):   #her test başlangıcında çalışacak fonk.
        self.driver = webdriver.Chrome()
        self.driver.get("https://demowebshop.tricentis.com/")
        self.driver.maximize_window()
        # self.dataClass = classData(self.driver)

    def teardown_method(self):  # her testin btiminde çalışacak fonk
        self.driver.quit()
    @pytest.mark.parametrize("senaryoturu,kelime,gerceklesen_sonuc",classData.getData())
    def test_arama_sonucu_uyarilari(self,senaryoturu,kelime,gerceklesen_sonuc):
        aramasayfasi = classAramaSayfasi(self.driver)
        aramasayfasi.arama_yap(kelime)
        if senaryoturu == 'negatif':
            mesaj=aramasayfasi.arama_uyari_mesajini_ver()
            sleep(2)
            assert mesaj == gerceklesen_sonuc
        elif senaryoturu.lower() == 'pozitif':
            urun_isimleri = aramasayfasi.webelement_textini_ver(aramasayfasi.DIAMOND_TEXT_CSS)
            for isim in urun_isimleri:

                assert kelime in isim.text
