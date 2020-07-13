from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dateutil.parser import parse
from post_info import get_post_info
import time
from utils import xpath

def get_posts(page, target_date, driver1, driver2):
    posts = []
    target_date = parse('{}T00:00:00.000Z'.format(target_date))
    post_date = parse('2020-07-13T03:04:53.000Z')
    posts_data = {}
    driver1.get('https://instagram.com.br/{}'.format(page))
    time.sleep(3)
    post_area = driver1.find_element(By.XPATH, xpath['post_area'])
    html = driver1.find_element(By.TAG_NAME, 'html')
    while target_date < post_date:
        for i in post_area.find_elements(By.TAG_NAME, "a"):
            if i.get_attribute('href') not in posts:
                posts_data['href'], post_date = get_post_info(i.get_attribute('href'), driver2)
                posts.append(i.get_attribute('href'))
        html.send_keys(Keys.PAGE_DOWN)
    return posts_data