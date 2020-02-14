from selenium import webdriver
import random
import time
browser=webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
link = "https://wifi.kyk.gov.tr/login.html"
browser.get(link)
time.sleep(2)
username = input("Kullanıcı adınızı giriniz: ")
password = input("Şifrenizi giriniz: ")
login = browser.find_element_by_xpath(" //*[@id='containerall']/form/table/tbody/tr[1]/td[2]/input")
passwd = browser.find_element_by_xpath(" //*[@id='containerall']/form/table/tbody/tr[2]/td[2]/input")
login.send_keys(username)
passwd.send_keys(password)
loginbutton = browser.find_element_by_xpath(" //*[@id='containerall']/form/table/tbody/tr[3]/td/input")
loginbutton.click()
time.sleep(7)
browser.close()