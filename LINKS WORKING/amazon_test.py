import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
options = Options()
options.add_argument('--incognito')
options.add_argument('--disable-notifications')
options.add_argument('--disable-popup-posting')
options.add_argument('--disable-popup-content')
options.add_argument('--disable-popup-images')
options.add_argument('--disable-popup-menu')
options.add_argument('--disable-popup-widgets')

driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.amazon.in")
driver.maximize_window()
time.sleep(10)

anchor_ele = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.TAG_NAME, "a")))

valid_links = []
for links in anchor_ele:
    href = links.get_attribute('href')
    if href and links.is_displayed():
        valid_links.append(href)

print("total links: " ,len(anchor_ele))
print(valid_links)

for link in valid_links:
    try:
        response = requests.get(link,timeout=5)
        if response.status_code == 200:
            print(f"Working:{link} (Status code: {response.status_code})")
        else:
            print(f"Not Working :{link} (Status code: {response.status_code})")
    except Exception as e:
        print(f" Error: {link} --> {str(e)}")

driver.quit()

