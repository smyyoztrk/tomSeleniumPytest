from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait #ilgili driverı bekleten yapı
from selenium.webdriver.support import expected_conditions as ec #beklenen koşullar
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
class test_tobeto:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://tobeto.com/giris")
        self.driver.maximize_window() #ekranı büyütür

    def chatbot(self):
        sleep(5)
        #self.driver.switch_to.frame(6)
        # self.driver.find_element(By.CSS_SELECTOR, ".exw-open-launcher__container").click()
  
        self.driver.switch_to.frame("exw-launcher-frame animated swing")
        sleep(3)
        chatbot_butonu = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CSS_SELECTOR,"button[id='launcher']")))
        chatbot_butonu.click()
        sleep(3)
        # tobeto_mesaj_kutusu = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CSS_SELECTOR,"h4[class='exw-title exw-with-avatar']")))
        # var_mı = tobeto_mesaj_kutusu.is_displayed()
        # print(var_mı)

        # self.driver.switch_to.frame(6)
        # sleep(5)
        # self.driver.find_element(By.CSS_SELECTOR, ".exw-open-launcher").click()

        
        
        
        # self.driver.switch_to.frame(6)
        # sleep(5)
        # self.driver.find_element(By.CSS_SELECTOR, ".exw-open-launcher").click()
        # sleep(3)

    def kayitol(self):
        service = Service()
        self.driver.execute_script("window.scrollBy(0,300)","")

        kayit_ol_buton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CSS_SELECTOR,"a[class='text-decoration-none text-muted fw-bold']"))).click()
        
        sleep(3)
        self.driver.execute_script("window.scrollBy(0,200)","")
        ad = self.driver.find_element(By.NAME,"firstName").send_keys("ali")
        soyad = self.driver.find_element(By.NAME,"lastName").send_keys("kaya")
        email = self.driver.find_element(By.NAME,"email").send_keys("abc@gmail.com")
        sifre = self.driver.find_element(By.NAME,"password").send_keys("1234")
        sifretekrar = self.driver.find_element(By.NAME,"passwordAgain").send_keys("1234")
        self.driver.execute_script("window.scrollBy(0,200)","")
        sleep(2)
        kayitolbutton2 = self.driver.find_element(By.CSS_SELECTOR,"button[class='btn btn-primary w-100 mt-6']").click()
        sleep(2)
        acıkrizametni = self.driver.find_element(By.NAME,"contact").click()
        uyeliksozlesmesi = self.driver.find_element(By.NAME,"membershipContrat").click()
        emailgonderimizni = self.driver.find_element(By.NAME,"emailConfirmation").click()
        aramaizni =self.driver.find_element(By.NAME,"phoneConfirmation").click()
        telno = self.driver.find_element(By.ID,"phoneNumber").send_keys("5551111111")
        self.driver.switch_to.frame("a-33q0cxqc9wuf")
        robotdegilim = self.driver.find_element(By.ID,"recaptcha-anchor").click()

        sleep(2)

        


denemeClass = test_tobeto()
#denemeClass.yanlis_girdi_basarisiz_giris()
#denemeClass.basarili_giris()
# denemeClass.bos_alanla_giris()
#denemeClass.basarili_sifre_yenileme()
#denemeClass.basarisiz_sifre_yenileme()
denemeClass.chatbot()
#denemeClass.kayitol()

