import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://www.amazon.in/")

actions = ActionChains(driver)
best_sellers = driver.find_element(By.LINK_TEXT,"Bestsellers")
best_sellers.click()

''' Add the all products in Cart '''
''' Add specific product or product is not available throw error '''


header = driver.find_element(By.XPATH,"//h2[text()='Bestsellers in Beauty']")
print(header.text)
driver.execute_script("arguments[0].scrollIntoView(true);", header)

driver.find_element(By.XPATH,"//a[@aria-label='Bestsellers in Beauty - See More']").click()
time.sleep(3)

beauty_items = driver.find_elements(By.XPATH,"//div[@class='_cDEzb_p13n-sc-css-line-clamp-3_g3dy1']")
scroll_to_last = driver.find_element(By.XPATH,"//a[text()='Next page']")
driver.execute_script("arguments[0].scrollIntoView(true);", scroll_to_last)
time.sleep(6)
print(len(beauty_items))

for i in beauty_items:
    print(i.text)

#driver.find_element(By.XPATH,"//input[@id='add-to-cart-button']").click()

# driver.find_element(By.LINK_TEXT,"Chemist At Play Exfoliating Body Wash 236ml | 4% (Salicylic Acid, Vitamin E and Lactic Acid) | Paraben & SLS Free | Gentle…").click()
#
# driver.find_element(By.XPATH,"//input[@name='submit.add-to-cart']").click()
#
# searchbar = driver.find_element(By.NAME,"field-keywords")
# searchbar.send_keys("playstation")
#
# suggestions = driver.find_elements(By.XPATH,"//div[@class='s-suggestion s-suggestion-ellipsis-direction']")
# print(len(suggestions))
#
# for i in suggestions:
#     print(i.text)
#     if i.text != "playstation with cd":
#         searchbar.clear()
#         searchbar.send_keys("playstation 5 pro")
#         searchbar.send_keys(Keys.ENTER)
#         break
#
# driver.find_element(By.XPATH,"//span[text()='Sony PlayStation5 Gaming Console (Slim)']").click()
# driver.switch_to.window(driver.window_handles[1])
# driver.find_element(By.XPATH,"//input[@name='submit.add-to-cart']").click()
# driver.find_element(By.NAME,"proceedToRetailCheckout").click()
# driver.find_element(By.XPATH,"//input[@id='ap_email_login']").send_keys("vinay@gmail.com")
# driver.find_element(By.XPATH,"//input[@class='a-button-input']").click()

