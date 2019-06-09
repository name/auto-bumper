from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Set username and password from config.ini

time.sleep(100)

usernameStr = open("config/login.txt", "r").readlines()[0]
passwordStr = open("config/login.txt", "r").readlines()[1]

print(usernameStr)
print(passwordStr)

time.sleep(100)

browser = webdriver.Chrome()
browser.get(('https://ogusers.com/member.php?action=login'))

browser.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Username/Email:'])[1]/following::input[1]").click()
browser.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Username/Email:'])[1]/following::input[1]").clear()
browser.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Username/Email:'])[1]/following::input[1]").send_keys(usernameStr)
browser.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Password:'])[1]/following::input[1]").click()
browser.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Password:'])[1]/following::input[1]").clear()
browser.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Password:'])[1]/following::input[1]").send_keys(passwordStr)
browser.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Password:'])[1]/following::input[3]").click()

time.sleep(100)

browser.get(('https://ogusers.com/Thread-add-me-on-steam--382587'))
browser.find_element_by_id("message").click()
browser.find_element_by_id("message").clear()
browser.find_element_by_id("message").send_keys("bumping to the top ty")
browser.find_element_by_id("quick_reply_submit").click()