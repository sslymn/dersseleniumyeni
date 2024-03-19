from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait    #sleep yerine kullanılacak yapı için bu şart
from selenium.webdriver.support import expected_conditions as EC # ayrıca expected_conditions yanına as ec şeklinde kısaltma yapabiliriz böylece uzun yazmak yerine ec yazıp geçebiliriz.
#sleep yerine kullanılacak yapının hangi şart ile beklencek olması için 
from selenium.webdriver.common.action_chains import ActionChains





class test_Saurce:
    def all_setting(self):
        driver =webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")  
        return driver
    


 
    #BAŞARISIZ GİRİŞ TESTİ
    def test_invalid_login(self):
        driver = self.all_setting()
        WebDriverWait(driver,5).until(EC.visibility_of_all_elements_located((By.ID,"user-name")))    
        userNameInput = driver.find_element(By.ID,"user-name")
        passwordInput = driver.find_element(By.ID,"password")
        sleep(1)
        userNameInput.send_keys("deneme")
        passwordInput.send_keys("1")
        WebDriverWait(driver,5).until(EC.visibility_of_all_elements_located((By.ID,"login-button")))   
        loginBtn = driver.find_element(By.ID,"login-button")
        loginBtn.click()
        errorMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
       #gereksinim dosyamızda nasıl olması gerektiği burada.
        testResult = errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
        print(f"BAŞARISIZ GİRİŞ TESTİ SONUCU: {testResult}")
        


    #-Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak "Epic sadface: Username is required" gösterilmelidir.
    def test_both(self):
        driver = self.all_setting()
        WebDriverWait(driver,5).until(EC.visibility_of_all_elements_located((By.ID,"user-name")))
        userName=driver.find_element(By.ID,"user-name")
        userName.send_keys("")
        password=driver.find_element(By.ID,"password")
        password.send_keys("")
        
        loginButton= driver.find_element(By.ID,"login-button")
        loginButton.click()
        
        errorMessage =driver.find_element(By.CSS_SELECTOR,"h3")
        testResult = errorMessage.text == "Epic sadface: Username is required"
        print(f"KULLANICI ADI VE ŞİFRE ALANLARININ BOŞ GEÇİLDİĞİ TESTİ SONUCU: {testResult}")


    #-Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak "Epic sadface: Password is required" gösterilmelidir.
    def fpassword(self):
        driver = self.all_setting()
        WebDriverWait(driver,5).until(EC.visibility_of_all_elements_located((By.ID,"user-name")))
        userName=driver.find_element(By.ID,"user-name")
        userName.send_keys("standard_user")
        password=driver.find_element(By.ID,"password")
        password.send_keys("")
        
        loginButton= driver.find_element(By.ID,"login-button")
        loginButton.click()
        
        errorMessage =driver.find_element(By.XPATH,"//div[@id='login_button_container']//form//h3")
        testResult = errorMessage.text == "Epic sadface: Password is required"
        print(f"ŞİFRE ALANININ  BOŞ GEÇİLDİĞİ TESTİ SONUCU: {testResult}")
    
    #-Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde "Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.
    def locked_out(self):
        driver = self.all_setting()
        userName=driver.find_element(By.ID,"user-name")
        userName.send_keys("locked_out_user")
        
        password=driver.find_element(By.ID,"password")
        password.send_keys("secret_sauce")
        
        loginButton= driver.find_element(By.ID,"login-button")
        loginButton.click()
        
        errorMessage =driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"ŞİFRE ALANININ  BOŞ GEÇİLDİĞİ TESTİ SONUCU: {testResult}")
    #-Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir. Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.   
    def login_list(self):
        driver = self.all_setting()
        userName=driver.find_element(By.ID,"user-name")
        userName.send_keys("standard_user")
        password=driver.find_element(By.ID,"password")
        password.send_keys("secret_sauce")
        loginButton= driver.find_element(By.ID,"login-button")
        loginButton.click()
        WebDriverWait(driver,5).until(EC.url_to_be("https://www.saucedemo.com/inventory.html"))

        p_list = driver.find_elements(By.CLASS_NAME,"inventory_item")
        testResult = len(p_list) == 6
        print(f"Görütülenen sayfada 6 adet ürün vardır.: {(testResult)}")
        

    #Başarılı giriş testi
    def t_login(self):
        driver = self.all_setting()
        WebDriverWait(driver,5).until(EC.visibility_of_all_elements_located((By.ID,"user-name")))
        userNameInput = driver.find_element(By.ID,"user-name")
        passwordInput = driver.find_element(By.ID,"password")
        sleep(1)
        userNameInput.send_keys("problem_user")
        passwordInput.send_keys("secret_sauce")
        WebDriverWait(driver,5).until(EC.visibility_of_all_elements_located((By.ID,"login-button")))   
        loginBtn = driver.find_element(By.ID,"login-button")
        loginBtn.click()
        
        expected_url = "https://www.saucedemo.com/inventory.html"
        actual_url = driver.current_url
        if actual_url == expected_url:
            print("Giriş başarılı.")
        else:
            print("Giriş başarısız.")
        


testClass = test_Saurce()
testClass.test_invalid_login()
testClass.test_both()
testClass.fpassword()
testClass.login_list()
testClass.t_login()
 



