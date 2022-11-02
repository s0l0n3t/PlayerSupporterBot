from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import selenium

def Web_scrapting(username_HQ,password_HQ):
    try:
        driver_path ="C:\PROJELER\PYTHON\Web_sraping\msedgedriver.exe"
#browser = webdriver.Edge(executable_path=driver_path)
        browser = webdriver.Edge()
#//*[@id="login_form"]/div/div/a
        browser.get("https://www.klanlar.org/")
        time.sleep(3)

        user_id = browser.find_element(By.NAME,"username")
        user_pass = browser.find_element(By.NAME,"password")
        user_id.send_keys(username_HQ)
        user_pass.send_keys(password_HQ)
        On_going = browser.find_element(By.XPATH,"//*[@id='login_form']/div/div/a")
        On_going.click()

        time.sleep(35)
        ongoing2 = browser.find_element(By.XPATH,"//*[@id='home']/div[3]/div[4]/div[10]/div[3]/div[2]/div[1]/a[2]/span")
        ongoing2.click()
        time.sleep(5)
        ongoing3 = browser.find_element(By.XPATH,"//*[@id='quickbar_contents']/ul/li[6]/span/a")
        ongoing3.click()
        time.sleep(5)
        premium_exchange = browser.find_element(By.XPATH,"//*[@id='id_exchange']/td/a")
        premium_exchange.click()
        time.sleep(3)
        wood_stock = browser.find_element(By.ID,"premium_exchange_rate_wood")
        time.sleep(1)
        stone_stock = browser.find_element(By.ID,"premium_exchange_rate_stone")
        time.sleep(1)
        iron_stock = browser.find_element(By.ID,"premium_exchange_rate_iron")

    
        for i in range(1,100):
            print("Wood",wood_stock.text)
            time.sleep(1)
            print("Stone",stone_stock.text)
            time.sleep(1)
            print("Iron",iron_stock.text)
    

    #for i in range(1,50):
     #   print(wood_stock.text)
      
    
        time.sleep(99999)
        browser.close()
    except Exception as Exception_Error:
        print(Exception_Error)

USER_ID = input()
USER_PASS = input()

Web_scrapting(USER_ID,USER_PASS)# Edge starter function.