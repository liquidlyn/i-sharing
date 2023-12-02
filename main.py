from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time
import os

driver = ''

def login():
    global driver
    loginid = input("FB帳號: ")
    loginpwd = input("密碼: ")

    service = Service(executable_path='./msedgedriver.exe')
    driver = webdriver.Edge(service=service)
    driver.maximize_window()
    driver.get('https://www.i-sharing.com.tw')

    driver.find_element(By.CLASS_NAME, 'intro__close').click()
    driver.find_element(By.CLASS_NAME, 'header__toggler').click()
    driver.find_element(By.LINK_TEXT, '請登入').click()

    driver.find_element(By.ID, 'email').send_keys(loginid)
    driver.find_element(By.ID, 'pass').send_keys(loginpwd)
    driver.find_element(By.ID, 'loginbutton').click()

window_before = ''

def cards():
    global driver, window_before
    driver.find_element(By.CLASS_NAME, 'header__toggler').click()
    driver.find_element(By.LINK_TEXT, '首頁').click()
    driver.find_element(By.CLASS_NAME, 'index__button.index__button-card.button').click()
    window_before = driver.window_handles[0]

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
        driver.find_element(By.CLASS_NAME, "button.btn-style.btn-line.books-line-share").click()
        time.sleep(2)
        # window_after = driver.window_handles[1]
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
    while True:
            try:        
                driver.find_element(By.CLASS_NAME, 'pop__close.text-hide.books-popup-close').click()
            except:
                continue
            break        
    print('Finished sucessfully.')

def shares(class_name):
    global driver, window_before
    driver.find_element(By.CLASS_NAME, class_name).click()
    # window_after = driver.window_handles[1]
    # driver.switch_to.window(window_after)
    # time.sleep(3)
    # driver.close()
    driver.switch_to.window(window_before)
    while True:
        try:        
            driver.find_element(By.CLASS_NAME, 'pop__close.text-hide.books-popup-close').click()
        except:
            continue
        break


def share():
    global driver
    driver.find_element(By.CLASS_NAME, 'header__toggler').click()
    driver.find_element(By.LINK_TEXT, '首頁').click()
    driver.find_element(By.CLASS_NAME, 'index__button.index__button-sharing.button').click()
    window_before = driver.window_handles[0]
    
    work = 1
    while True:
        if work == 1:
            refresh = int(input('請輸入刷新次數，至少為1：\n若需跳出分享訊息模式，輸入數字0'))
            if refresh == 0: break
            for j in range(refresh):
                for i in range(6):
                    try:        
                        shares('button.btn-style.btn-fb')
                    except:
                        continue
                    try:
                        shares('button.btn-style.btn-line')
                    except:
                        break

                try:
                    driver.find_element(By.CLASS_NAME, 'news-more.btn-plus-more').click()
                    print('目前已刷新'+str(j+1)+'次')
                except:
                    work = 0
                    for i in range(6):
                        try:        
                            shares('button.btn-style.btn-fb')
                        except:
                            continue
                        try:
                            shares('button.btn-style.btn-line')
                        except:
                            break
                    print('已刷新至底，且完成所有分享')
                    break
        else:
            break

mode = int(input('進入模式1：製作卡片/模式2：分享訊息？ [1|2]'))
if mode == 1:
    login()
    cards()
    input('送出任意鍵進入分享訊息模式')
    share()
    input('結束')

if mode == 2:
    login()
    share()
    input('送出任意鍵進入製作卡片模式')
    cards()
    input('結束')
