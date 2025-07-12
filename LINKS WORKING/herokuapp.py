import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


Service = Service(ChromeDriverManager().install())
options = Options()
driver = webdriver.Chrome(service=Service, options=options)
driver.maximize_window()

''' https://imagility.co/ '''
''' links count and verify the link is working or not'''

driver.get("https://imagility.co/")
time.sleep(5)

anchor_ele = driver.find_elements(By.TAG_NAME, "a")

linksList = []
for elem in anchor_ele:
    href = elem.get_attribute('href')
    if href is not None:
        linksList.append(href)

print('Total links:', len(linksList))
print(linksList)

for links in anchor_ele:
    print(links.get_attribute('href'))

for link in linksList:
    try:
        response = requests.get(link, timeout=5)
        if response.status_code == 200:
            print(f" Working: {link} (Status code: {response.status_code})")
        else:
            print(f" Not Working : {link} (Status code: {response.status_code})")
    except Exception as e:
        print(f" Error: {link} --> {str(e)}")

driver.quit()






































# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(10)
#
# driver.get("https://the-internet.herokuapp.com/")
# driver.find_element(By.LINK_TEXT,"Broken Images").click()
# imgs = driver.find_elements(By.XPATH,"//div/img")
# print(len(imgs))
#
# for i in imgs:
#     print(i.get_attribute("src"))
