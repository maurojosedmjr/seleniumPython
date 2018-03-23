from selenium import webdriver
import time
import os
from sys import exit

chromedriver = "./chromedriver_linux64/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver

browser = webdriver.Chrome(chromedriver)

URL = 'https://www.kabum.com.br/'

try:
    browser.get(URL)
except Exception as e:
    print e
    exit(0)

time.sleep(10)
popup = browser.find_element_by_class_name('b-close')
popup.click()
time.sleep(2)
processador=browser.find_element_by_xpath('//*[@id="menu_left"]/div[8]/p[12]/a')
processador.click()
time.sleep(5)
browser.close()
