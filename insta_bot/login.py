## Instagram Login
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from utils import *

def login (username, password):
    driver = Firefox(executable_path=gecko_path)
    driver.get("https://instagram.com.br")
    time.sleep(3)
    driver.find_element(By.XPATH, xpath['username']).send_keys(username)
    driver.find_element(By.XPATH, xpath['password']).send_keys(password, Keys.ENTER)
    return driver