"""from selenium import webdriver
from selenium.webdriver.remote import switch_to
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

''' Types of Methods in Selenium '''
"Browser Methods"
driver.get()
driver.close()
driver.quit()
driver.maximize_window()

"Navigation Methods"
driver.back()
driver.forward()
driver.refresh()

"Element Methods - Interact with web elements"
find_element()
find_elements()
click()
send_keys()
clear()
is_displayed()
is_enabled()
id_selected()

"Wait Methods"
driver.implicitly_wait(5)
WebDriverWait() + ExpectedConditions

"Alert and Frame Methods"
switch_to.alert()
switch_to.frame()
switch_to.default_content()"""
import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get('https://www.orangehrm.com/en/30-day-free-trial')


# dropdownlist = driver.find_elements(By.ID,"Form_getForm_Country")
#
# clist = []
# for i in dropdownlist:
#     clist.append(i.text)
#
# print(clist)

action = ActionChains(driver)

hover = driver.find_element(By.XPATH,"//a[text()='Solutions']")
action.move_to_element(hover).perform()

right_click = driver.find_element(By.NAME,"Email")
action.context_click(right_click).perform()

double_click = driver.find_element(By.ID,"Form_getForm_subdomain")
action.double_click(double_click).perform()

