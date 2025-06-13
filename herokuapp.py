from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://the-internet.herokuapp.com/")
driver.find_element(By.LINK_TEXT,"Broken Images").click()
imgs = driver.find_elements(By.XPATH,"//div/img")
print(len(imgs))

for i in imgs:
    print(i.get_attribute("src"))
