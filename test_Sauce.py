from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait    #sleep yerine kullanılacak yapı için bu şart
from selenium.webdriver.support import expected_conditions  # ayrıca expected_conditions yanına as ec şeklinde kısaltma yapabiliriz böylece uzun yazmak yerine ec yazıp geçebiliriz.
#sleep yerine kullanılacak yapının hangi şart ile beklencek olması için 
from selenium.webdriver.common.action_chains import ActionChains





class test_Saurce:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
 
    #BAŞARISIZ GİRİŞ TESTİ
    def test_invalid_login(self):   #kişinin doğru giriş yapmadığı seneryoyu test edecek fonksiyon 
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_all_elements_located((By.ID,"user-name")))    
        #burada By.ID,"user-name" locaterını tekrar parantez içine yazdık sebebi tek koşul olarak yazmak için yoksa hata alırız.  
        #until şuna kadar anlamında expected_conditions içinden biri verilir.   
        #burada driver ve timeout yerleri zorunlu timeout anlamı max şu kadar bekle kullanımı için 
        #SLEEP YERİNE ASIL KULLANILACAK ŞEKİL ŞU MANTIKTA OLACAK = en fazla 5 saniye olacak şekilde user-name idli elementin görünmesini bekle
        userNameInput = self.driver.find_element(By.ID,"user-name")
        passwordInput = self.driver.find_element(By.ID,"password")
        sleep(2)
        userNameInput.send_keys("deneme")
        passwordInput.send_keys("1")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_all_elements_located((By.ID,"login-button")))   
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
       #gereksinim dosyamızda nasıl olması gerektiği burada.
        testResult = errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
        print(f"TEST SONUCU: {testResult}")
      
     
       

        


testClass = test_Saurce()
testClass.test_invalid_login()

 



