from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options
import time
import message_




USER_ID = input()
USER_PASS = input()

def main(username_HQ,password_HQ):
    try:
        message_.main()     
#browser = webdriver.Edge(executable_path='msedgedriver.exe') use if you dont have driver
        browser = webdriver.Edge()
#//*[@id="login_form"]/div/div/a
        browser.get("https://www.klanlar.org/")
        time.sleep(1)

        user_id = browser.find_element(By.NAME,"username")
        user_pass = browser.find_element(By.NAME,"password")
        user_id.send_keys(username_HQ)
        user_pass.send_keys(password_HQ)
        On_going = browser.find_element(By.XPATH,"//*[@id='login_form']/div/div/a")
        On_going.click()
        
        world_clickable = WebDriverWait(browser,500).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='home']/div[3]/div[4]/div[10]/div[3]/div[2]/div[1]/a[2]/span"))).click()
        #We have to run once.
        
        quickbar_bazaar_clickable = WebDriverWait(browser,500).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='quickbar_contents']/ul/li[6]/span/a"))).click()
       # ongoing3 = browser.find_element(By.XPATH,"//*[@id='quickbar_contents']/ul/li[6]/span/a")
       # ongoing3.click()
       # premium_exchange = browser.find_element(By.XPATH,"//*[@id='id_exchange']/td/a")
        # premium_exchange.click()
        premium_exchange_clickable = WebDriverWait(browser,500).until(EC.presence_of_element_located((By.XPATH,"//*[@id='id_exchange']/td/a"))).click()
        wood_stock = browser.find_element(By.ID,"premium_exchange_rate_wood")
        time.sleep(1)
        stone_stock = browser.find_element(By.ID,"premium_exchange_rate_stone")
        time.sleep(1)
        iron_stock = browser.find_element(By.ID,"premium_exchange_rate_iron")
        
        while(True):
                message_.RAW_WOOD = browser.find_element(By.ID,"wood").text
                message_.RAW_STONE = browser.find_element(By.ID,"stone").text
                message_.RAW_IRON = browser.find_element(By.ID,"iron").text
                if (int(wood_stock.text[0:3]) <= 200 or int(stone_stock.text[0:3]) <= 200 or int(iron_stock.text[0:3]) <= 200):
                        
                        message_.token_updater.dispatcher.bot.send_message(chat_id=message_.mytelegram_id,text='Wood %s'%(wood_stock.text))
                        message_.token_updater.dispatcher.bot.send_message(chat_id=message_.mytelegram_id,text='Stone %s'%(stone_stock.text))
                        message_.token_updater.dispatcher.bot.send_message(chat_id=message_.mytelegram_id,text='Iron %s'%(iron_stock.text))
                        time.sleep(5)
                #Do not return to main()
       
      #  browser.close()
    except Exception as Exception_Error:
        print(Exception_Error)
        return


main(USER_ID,USER_PASS)# Edge starter function.