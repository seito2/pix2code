import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import os
import requests
from tqdm import tqdm

options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(options=options)


filenames = []
path = "../code"

for file in os.listdir(path):
    base, ext = os.path.splitext(file)
    if ext == '.html':
        filenames.append(base)


for index, filename in enumerate(tqdm(filenames)):
    try:
        # set driver and url
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--hide-scrollbars')
        driver = webdriver.Chrome(options=options)
        driver.set_window_size(1200, 800)
        driver.get(f"http://localhost:8000/code/{filename}.html")
        # get width and height of the page
        w = driver.execute_script("return document.body.scrollWidth;")
        h = driver.execute_script("return document.body.scrollHeight;")

        # set window size
        driver.set_window_size(1200,h)

        WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located)

        time.sleep(10)

        # Get Screen Shot
        driver.save_screenshot(f"./output/{filename}-pc.png")
        
        
        driver.set_window_size(375, 800)
        h = driver.execute_script("return document.body.scrollHeight;")
        driver.set_window_size(375, h)
        driver.save_screenshot(f"./output/{filename}-sp.png")
        driver.close()

        response = requests.get(url, timeout=(10.0))

        with open(f'./output/{filename}.html', 'w', encoding="utf_8_sig") as f:
            f.write(response.text)
    except:
        continue