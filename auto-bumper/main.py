# OGUsers Autobumper
import configparser, time, warnings, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Disable python logging to console
warnings.filterwarnings("ignore")
clear = lambda: os.system('cls')
clear()
# Setup web-driver
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--hide-scrollbars')
options.add_argument('--disable-gpu')
options.add_argument("--log-level=3")
browser = webdriver.Chrome(chrome_options=options)
clear()

# TODO
# - Clean up config file to make settings thread urls and comments more user friendly
# - Research how to protect python code and run as executable
# - Login via personal api and check hwid against system
# - HWID Lock
# - site for users to request hwid -> username/hwid/email

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        # Goes to login page and user details from config.ini
        browser.get(('https://ogusers.com/member.php?action=login'))
        browser.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Username/Email:'])[1]/following::input[1]").send_keys(self.username)
        browser.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Password:'])[1]/following::input[1]").send_keys(self.password)
        browser.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Password:'])[1]/following::input[3]").click()
        time.sleep(1)

    def bump(self):
        # Gets list of threads+comments then splits them to single values
        threads = config['user']['threads'].split(',')
        while True:
            for thread in threads:
                thread_url = thread.split('^')[0]
                thread_comment = thread.split('^')[1]
                print('[!] Bumping thread ' + thread_url + ' with comment ' + thread_comment + ' ..')
                # Goes to thread
                browser.get((thread_url))
                # Writes out custom comment
                browser.find_element_by_id("message").send_keys(thread_comment)
                browser.find_element_by_id("quick_reply_submit").click()
                print('[!] Bumped!')
                time.sleep(31)
            print('[-] Bumped all threads, waiting 1 hour and starting again..')
            time.sleep(3610)

# Read config file and grab username/password
config = configparser.ConfigParser()
config.read('config.ini')

# Set user details
OGU = User(config['user']['username'], config['user']['password'])
# Start bumping
print('[-] Logging in..')
OGU.login()
print('[+] Logged in..')
print('[+] Starting bumper..')
OGU.bump()