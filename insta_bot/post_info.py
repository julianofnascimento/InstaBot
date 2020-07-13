from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from utils import xpath
from dateutil.parser import parse

def get_likers(driver2):
    time.sleep(3)
    driver2.find_element(By.XPATH, xpath['likers_button']).click()
    likers_body = WebDriverWait(driver2, 10).until(EC.presence_of_element_located((By.XPATH, xpath['likers_div'])))
    time.sleep(3)
    likers = []
    previous_len=-1
    while len(likers)>previous_len:
        previous_len = len(likers)
        elements = likers_body.find_elements(By.TAG_NAME, 'a')
        for el in elements:
            if el.get_attribute('title') and el.get_attribute('title') not in likers:
                likers.append(el.get_attribute('title'))
        driver2.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", likers_body)
        time.sleep(1)
    return likers

def get_post_info(post_link, driver2):
    driver2.get(post_link)
    date = WebDriverWait(driver2, 10).until(EC.presence_of_element_located((By.XPATH, xpath['post_date']))).get_attribute('datetime')
    date = parse(date)
    likers = ['This is a video']
    try:
        likers = get_likers(driver2)
    except:
        pass
    return likers, date