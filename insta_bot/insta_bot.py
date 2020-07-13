## Get post likers
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import xpath
from login import login
import time
from dateutil.parser import parse
from posts_handler import get_posts

def get_page_data(target_page, target_date, username, password):
    driver1 = login(username, password)
    time.sleep(4)
    driver2 = login(username, password)
    time.sleep(4)
    posts_data = get_posts(target_page, target_date, driver1, driver2)
    return posts_data
