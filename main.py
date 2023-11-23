from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time
import os

loginid = input("FB帳號: ")
loginpwd = input("密碼: ")

service = Service(executable_path='./msedgedriver.exe')
driver = webdriver.Edge(service=service)
driver.maximize_window()
driver.get('https://www.i-sharing.com.tw/card/main')


while True:
    try:        
        driver.find_element(By.CLASS_NAME,'pop__close.text-hide.books-popup-close').click()
    except:
        continue
    break

driver.find_element(By.CLASS_NAME, 'header__toggler').click()
driver.find_element(By.LINK_TEXT, '請登入').click()

driver.find_element(By.ID, 'email').send_keys(loginid)
driver.find_element(By.ID, 'pass').send_keys(loginpwd)
driver.find_element(By.ID, 'loginbutton').click()

for i in range(10):
    while True:
        try:        
            driver.find_element(By.CLASS_NAME, 'pop__close.text-hide.books-popup-close').click()
        except:
            continue
        break

    driver.find_element(By.LINK_TEXT, '立即寄送璀璨時刻').click()

    time.sleep(1)
    driver.find_element(By.XPATH, '//img[@src="https://jci.i-sharing.com.tw/assets/images/greeting/img-video1.jpg"]').click()
    driver.find_element(By.XPATH, '//img[@src="https://jci.i-sharing.com.tw/assets/images/greeting/img-video2.jpg"]').click()
    driver.find_element(By.XPATH, '//img[@src="https://jci.i-sharing.com.tw/assets/images/greeting/img-video3.jpg"]').click()
    driver.find_element(By.XPATH, '//img[@src="https://jci.i-sharing.com.tw/assets/images/greeting/img-video4.jpg"]').click()
    driver.find_element(By.CLASS_NAME, 'button.btn-style.btn.next').click()

    driver.find_element(By.XPATH, '//img[@src="https://jci.i-sharing.com.tw/assets/images/greeting/img-isharing.png"]').click()
    step = driver.find_element(By.ID, 'box-step-2')
    step.find_element(By.CLASS_NAME, 'button.btn-style.btn.next').click()

    driver.find_element(By.CLASS_NAME, 'button.btn-style.btn-event.btn.next').click()

    driver.find_element(By.CLASS_NAME, "input-file").send_keys(os.getcwd()+"\\cat-18.jpg")
    driver.find_element(By.CLASS_NAME, "input-text").send_keys("name1")
    inputt = driver.find_element(By.CLASS_NAME, "name.recipient")
    inputt.find_element(By.CLASS_NAME, "input-text").send_keys("name2")
    driver.find_element(By.CLASS_NAME, "message").send_keys("msg")
    step = driver.find_element(By.ID, 'box-step-4')
    step.find_element(By.CLASS_NAME, 'button.btn-style.btn.next').click()

    step = driver.find_element(By.ID, 'box-step-5')
    step.find_element(By.CLASS_NAME, 'button.btn-style.btn.next').click()

    time.sleep(4)
    window_before = driver.window_handles[0]
    driver.find_element(By.CLASS_NAME, "button.btn-style.btn-line.books-line-share").click()
    time.sleep(2)
    window_after = driver.window_handles[1]
    # driver.switch_to.window(window_after)
    # driver.close()
    driver.switch_to.window(window_before)

    while True:
        try:        
            driver.find_element(By.CLASS_NAME, 'pop__close.text-hide.books-popup-close').click()
        except:
            continue
        break

    driver.find_element(By.LINK_TEXT, "再寄一張賀卡").click() 

    if i <8:
            print('No.'+str(i+1)+' card is completed, there are '+str(9-i)+' unfinished cards.')
    if i==8:
        print('No.'+str(i+1)+' card is completed, there is 1 unfinished card.')
        
input('Finished sucessfully.')