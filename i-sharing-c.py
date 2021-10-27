from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

loginid = input("FB帳號: ")
loginpwd = input("密碼: ")

driver = webdriver.Edge(r"C:\Users\user\Desktop\msedgedriver.exe")
driver.get('https://www.i-sharing.com.tw/card/main')

driver.find_element_by_class_name('menu-toggler.menu-toggler-open.pos-a').click()
driver.find_element_by_class_name('books-fb-name').click()
driver.find_element_by_id('email').send_keys(loginid)
driver.find_element_by_id('pass').send_keys(loginpwd)
driver.find_element_by_id('loginbutton').click()

time.sleep(2)
for i in range(11):
    driver.find_element(By.ID, "btn-create-card").click()
    time.sleep(1)
    if i !=0:
        for times in range(i):
            driver.find_element(By.CSS_SELECTOR, ".box-content > .swiper > .swiper-button-next").click()
            
    driver.find_element(By.LINK_TEXT, "下一步").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".input-text:nth-child(2)").send_keys("name1")
    driver.find_element(By.CSS_SELECTOR, ".input-text:nth-child(3)").send_keys("name2")
    driver.find_element(By.LINK_TEXT, "下一步").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "#box-step-3 .message").send_keys("content**")

    driver.find_element(By.CSS_SELECTOR, ".input-file").send_keys(os.getcwd()+"\\cat-18.jpg")
    driver.find_element(By.LINK_TEXT, "下一步").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "下一步").click()
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, "btn.btn-cta.kerning-2.pink.skip").click()
    
    time.sleep(3)
    driver.find_element(By.CLASS_NAME, "btn.btn-event.kerning-2.books-card-complete").click()
    time.sleep(1)
    
    window_before = driver.window_handles[0]
    driver.find_element(By.CSS_SELECTOR, ".btn-share-line").click()
    time.sleep(2)
    window_after = driver.window_handles[1]
    driver.switch_to_window(window_after)
    driver.close()
    driver.switch_to_window(window_before)
    driver.find_element(By.LINK_TEXT, "關閉").click()
    driver.find_element(By.LINK_TEXT, "再寄一張賀卡").click()

input('Please insert any key to exit.')   