# OGUsers Autobumper
import configparser, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup web-driver
browser = webdriver.Chrome()

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        browser.get(('https://ogusers.com/member.php?action=login'))
        browser.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Username/Email:'])[1]/following::input[1]").send_keys(self.username)
        browser.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Password:'])[1]/following::input[1]").send_keys(self.password)
        browser.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Password:'])[1]/following::input[3]").click()
        
    def bump(self):
        threads = config['user']['threads'].split(',')
        for thread in threads:
            browser.get((thread))
            browser.find_element_by_id("message").send_keys("bumping to the top ty")
            browser.find_element_by_id("quick_reply_submit").click()
            time.sleep(100)

# Read config file and grab username/password
config = configparser.ConfigParser()
config.read('config.ini')

# Set user details
OGU = User(config['user']['username'], config['user']['password'])
OGU.login()
OGU.bump()