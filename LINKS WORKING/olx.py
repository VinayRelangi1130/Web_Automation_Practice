from http.client import responses

import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
options = Options()

driver = webdriver.Chrome(service=service, options=Options())

driver.get("https://www.olx.in/")
driver.maximize_window()
driver.implicitly_wait(5)

anchor_elements = driver.find_elements(By.TAG_NAME, "a")

valid_links = []
for links in anchor_elements:
    href = links.get_attribute('href')
    if href and links.is_displayed():
        valid_links.append(href)

print("total links: ", {len(anchor_elements)})
print(valid_links)

for link in valid_links:
    try:
        responses = requests.get(link,timeout=10)
        if responses.status_code == 200:
            print(f"Working ---> {link} -->  (Status code: {responses.status_code})")
        else:
            print(f"Not Working ---> {link} --> (Status code: {responses.status_code})")
    except Exception as error:
        print(f" Error: {link} --> {str(error)}")

driver.quit()
