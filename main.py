from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

loginid = input("FB帳號: ")
loginpwd = input("密碼: ")

driver = webdriver.Edge("msedgedriver.exe")
driver.get('https://www.i-sharing.com.tw/card/main')

driver.find_element(By.CLASS_NAME,'header__menu__icon.books-menu-open').click()
driver.find_element(By.CLASS_NAME,'books-fb-name').click()
driver.find_element(By.ID,'email').send_keys(loginid)
driver.find_element(By.ID,'pass').send_keys(loginpwd)
driver.find_element(By.ID,'loginbutton').click()
time.sleep(2)

for i in range(10):
    while True:
        try:        
            driver.find_element(By.LINK_TEXT, "立即打造").click()
            time.sleep(1)
        except:
            continue
        break
    while True:
        try:        
            driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/section[1]/div/picture['+str(i+1)+']/img').click()
            time.sleep(1)
        except:
            continue
        break
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, "greeting__step2-from").send_keys("name1")
    driver.find_element(By.CLASS_NAME, "greeting__step2-to").send_keys("name2")
    driver.find_element(By.CLASS_NAME, "greeting__step2-textarea").send_keys("msg")
    driver.find_element(By.CLASS_NAME, "greeting__step2-input-upload").send_keys(os.getcwd()+"\\cat-18.jpg")
    for j in range(2):
        while True:
            try:        
                driver.find_element(By.LINK_TEXT, "下一步").click()
                time.sleep(1)
            except:
                continue
            break
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "完成賀卡").click()
    time.sleep(3)
    
    window_before = driver.window_handles[0]
    while True:
        try:        
            driver.find_element(By.CLASS_NAME, "greeting__share-btn--line").click()
            time.sleep(1)
        except:
            continue
        break
    time.sleep(3)
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    driver.close()
    driver.switch_to.window(window_before)
    while True:
        try:        
            driver.find_element(By.CLASS_NAME, "books-popup-close").click()
            time.sleep(1)
        except:
            continue
        break
    while True:
        try:        
            driver.find_element(By.LINK_TEXT, "再寄一張賀卡").click()
            time.sleep(1)
        except:
            continue
        break
    if i <8:
        print('No.'+str(i+1)+' card is completed, there are '+str(9-i)+' unfinished cards.')
    if i==8:
        print('No.'+str(i+1)+' card is completed, there is 1 unfinished card.')
    
    
input('Finished sucessfully.')
