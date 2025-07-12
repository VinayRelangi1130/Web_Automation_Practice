import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://animesalt.com/")

home_btn = driver.find_element(By.XPATH,"//a[@id='homeButton']")
home_btn.click()

language_select = driver.find_element(By.XPATH,"//div[text()='Telugu']")
driver.execute_script("arguments[0].click();", language_select)

time.sleep(3)

symbols = driver.find_element(By.XPATH,"//div[text()='Search']")
symbols.click()
time.sleep(3)

search = driver.find_element(By.ID,"tr_live_search")
search.send_keys("naruto")
search.send_keys(Keys.ENTER)

series = driver.find_element(By.XPATH,"//a[@href='https://animesalt.cc/series/naruto-shippuden/']")
driver.execute_script("arguments[0].click();", series)
time.sleep(2)

Seasons = driver.find_element(By.XPATH,"//button[text()='Season']")

seasons_select = driver.find_elements(By.XPATH,"//li[@class='sel-temp']/a")
print(len(seasons_select))

for season in seasons_select:
    print(season.text)
    if season.text == "Season 7":
        season.click()
        time.sleep(2)
        break

episode_names =driver.find_elements(By.CLASS_NAME,"entry-title")
print(len(episode_names))

for episode in episode_names:
    print(episode.text)
    if episode.text == "Separation":
        episode.click()
        break



read_more = driver.find_element(By.XPATH,"//button[@id='overview-toggle']")
read_more.click()

page_last = driver.find_element(By.ID,"reply-title")
driver.execute_script("arguments[0].scrollIntoView(true);", page_last)

textarea = driver.find_element(By.XPATH,'//p[@class="comment-form-comment"]/textarea')
textarea.send_keys("Excellent Series")

name = driver.find_element(By.XPATH,"//input[@id='author']")
name.send_keys("vinay")

email = driver.find_element(By.XPATH,"//input[@id='email']")
email.send_keys("fsijjsj@gmail.com")

submit_btn = driver.find_element(By.XPATH,"//input[@name='submit']")
submit_btn.click()

time.sleep(2)
driver.quit()
