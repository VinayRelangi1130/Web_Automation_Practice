# import time
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# # open chrome and maximizing the window
# driver = webdriver.Chrome()
# driver.maximize_window()
# wait = WebDriverWait(driver, 10)
#
# # open url
# driver.get("https://www.abhibus.com/")
# driver.implicitly_wait(10)
#
# from_loc = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@placeholder='Leaving From']")))
# ''' need if else conditions and assertions  '''
#
#
# from_loc.send_keys("@#$ada@")
# time.sleep(2)
# from_loc.send_keys(Keys.ENTER)
#
# to_loc = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@placeholder='Going To']")))
# to_loc.send_keys("hyderabad")
# time.sleep(2)
# to_loc.send_keys(Keys.ENTER)
#
# Tomorrow_btn = driver.find_element(By.XPATH,"//a[text()='Tomorrow']")
# Tomorrow_btn.click()
# time.sleep(3)
#
# Bus_type_AC_option = wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='AC']")))
# Bus_type_AC_option.click()
# time.sleep(3)
#
# Sleeper_Bus_option = wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Sleeper']")))
# Sleeper_Bus_option.click()
#
# Drop_time = wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='5 PM - 11 PM']")))
# Drop_time.click()
#
# Sort_by_Price = wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Price']")))
# Sort_by_Price.click()
#
# Sort_by_Ratings = wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Ratings']")))
# Sort_by_Ratings.click()
#
# Sort_by_Arrival_Time = wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Arrival Time']")))
# Sort_by_Arrival_Time.click()
#
# Sort_by_Departure_Time = wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Departure Time']")))
# Sort_by_Departure_Time.click()
#
# select_btn = wait.until(EC.element_to_be_clickable((By.XPATH,"show-service-btn-2844556830")))
# select_btn.click()
#
# driver.find_element(By.XPATH,"//*[@id='seat-layout-details']/tbody/tr[2]/td[10]/div/button/span").click()
# driver.find_element(By.XPATH,"//input[@placeholder='Search Boarding Point']").send_keys("PR College")
#
# driver.find_element(By.XPATH,"//p[text()='PR College']").click()
# time.sleep(3)
#
# driver.find_element(By.XPATH,"//input[@placeholder='Search Dropping Point']").send_keys("Miyapur")
# driver.find_element(By.XPATH,"//p[text()='Miyapur']").click()
# time.sleep(3)
#
# driver.find_element(By.XPATH,"//button[text()='Proceed']").click()
# time.sleep(2)
#
# driver.quit()




