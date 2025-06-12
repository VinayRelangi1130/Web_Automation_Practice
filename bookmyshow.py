# from selenium import webdriver
# from selenium.webdriver import Keys
# from selenium.webdriver.common.by import By
# import time
#
# driver = webdriver.Chrome()
# driver.maximize_window()
#
#
# driver.get("https://in.bookmyshow.com/")
#
# search = driver.find_element(By.XPATH,"//input[@placeholder='Search for your city']")
# search.send_keys("kakinada")
#
# driver.find_element(By.XPATH,"//span[text()='View All Cities']").click()
#
# cities = driver.find_elements(By.XPATH,"//li[@class='bwc__sc-ttnkwg-7 hcyBjM']/div")
# time.sleep(2)
#
# for city in cities:
#     if city.text == "Kakinada":
#         city.click()
#         break
#
#
# driver.find_element(By.XPATH,"//a[text()='Movies']").click()
# time.sleep(2)
#
# movies = driver.find_elements(By.XPATH,"//div[@class='sc-7o7nez-0 elfplV']")
# print(len(movies))
#
# for movie in movies:
#     if movie.text == "Subham" :
#         movie.click()
#         break
#
#
# time.sleep(2)
# driver.quit()
