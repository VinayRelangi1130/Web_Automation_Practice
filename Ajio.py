import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from unicodedata import category

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.ajio.com")

action_chains = ActionChains(driver)

''' Hover elements printing in console and assertions '''
men = driver.find_element(By.XPATH,"//span[text()='MEN']")
action_chains.move_to_element(men).perform()
time.sleep(2)

categories = driver.find_element(By.XPATH,"//a[text()='CATEGORIES']")
action_chains.move_to_element(categories).perform()
time.sleep(2)

category_links = driver.find_elements(By.XPATH,"//div[@class='title']/a/span/strong")

for i in category_links:
    print(i.text)
    if i.text == "INNERWEAR" :
        break

sub_links = driver.find_elements(By.XPATH,"//div[@class='items']/span/a")

for j in sub_links:
    print(j.text)
    if j.text == "Ramraj Dhotis":
        break

brands = driver.find_element(By.XPATH,"//a[text()='Brands']")
action_chains.move_to_element(brands).perform()
time.sleep(2)

brand_links = driver.find_elements(By.XPATH,"//div[@class='title']/a/span/strong")

for a in brand_links:
    print(a.text)
    if a.text == "A-Z BRANDS" :
        break


sub2_links = driver.find_elements(By.XPATH,"//div[@class='items']/span/a")

for b in sub2_links:
    print(b.text)
    if b.text == "Woodland":
        break


go_to_bottom = driver.find_element(By.XPATH,"//strong[text()='Payment Methods']")
driver.execute_script("arguments[0].scrollIntoView(true);", go_to_bottom)
time.sleep(2)

driver.execute_script("window.scrollTo(document.body.scrollHeight,0);")
time.sleep(2)

search_bar = driver.find_element(By.XPATH,"//input[@name='searchVal']")
search_bar.send_keys("nike shoes")
search_bar.send_keys(Keys.ENTER)
time.sleep(2)

search_result = driver.find_elements(By.CLASS_NAME,"higlighted-text")
print(len(search_result))

for res in search_result:
    print(res.text)
    if res.text == "nike shoes":
        search_bar.clear()
        search_bar.send_keys("Men Nike Sports Shoes")
        search_bar.send_keys(Keys.ENTER)
        break


''' Access Denied 
Access Denied
You don't have permission to access "http://www.ajio.com/" on this server.
Reference #18.55b22c31.1751893487.40e91c32

https://errors.edgesuite.net/18.55b22c31.1751893487.40e91c32
'''