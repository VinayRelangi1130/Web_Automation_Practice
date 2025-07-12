import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)

driver.get("https://www.justickets.in/cities")


cities = []
try:
    find_city = driver.find_elements(By.XPATH, "//div[@class='state']/div/div")
    for city in find_city:
        cities.append(city.text)

    assert len(cities) > 0, "City List is empty"
    print("total cities: ", len(find_city))

except Exception as e:
    print("Error",e)

print(cities)

try:
    search = driver.find_element(By.XPATH,"//input[@class='search']")
    search.click()
    a = False
    for city in cities:
        print(city)
        if city.strip().lower() == "kakinada" :
            search.clear()
            search.send_keys(city)
            driver.find_element(By.XPATH,"//div[text()='Kakinada']").click()
            print(city, "selected successfully")
            a = True
            break
    assert a, "city not found"

except Exception as e:
    print("Error",e)

copyrights = driver.find_element(By.XPATH,"//div[@class='cc']")
driver.execute_script("arguments[0].click();", copyrights)

Bookings = driver.find_element(By.XPATH,"//p[text()='Bookings Open']")
driver.execute_script("arguments[0].click();", Bookings)

# driver.find_element(By.XPATH,"//span[text()='Any Movie']").click()
# driver.find_element(By.XPATH,"//span[text()='Bhairavam']").click()
#
# driver.find_element(By.XPATH,"//span[text()='Any Theatre']").click()
# driver.find_element(By.XPATH,"//span[text()='GEPL Padmapriya Sripriya']").click()
# time.sleep(2)
# driver.find_element(By.XPATH,"//span[text()='Padmapriya Dolby Atmos']").click()
#
# driver.find_element(By.XPATH,"//span[text()='Any Date']").click()
# driver.find_element(By.XPATH,"//span[text()='Thursday, 12 Jun']").click()
#
# driver.find_element(By.XPATH,"//span[text()='Any Time']").click()
# driver.find_element(By.XPATH,"//span[text()='Night']").click()
# time.sleep(1)
# driver.find_element(By.XPATH,"//span[text()='09:30 PM']").click()
#
# driver.find_element(By.XPATH,"//a[text()='9:30 PM']").click()
# time.sleep(4)
#
# driver.find_element(By.XPATH,"//div[text()='F3']").click()
#
# driver.find_element(By.XPATH,"//span[text()='Book Now']").click()
# time.sleep(2)
#
# accept = wait.until(EC.presence_of_element_located((By.XPATH,"//button[text()='Accept']")))
# accept.click()
# time.sleep(4)
#
# enter_promocode = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@placeholder='Enter Promo Code, If Available']")))
# enter_promocode.send_keys("412578633")
# time.sleep(2)
# driver.find_element(By.XPATH,"//button[text()='Apply']").click()
# time.sleep(1)
#
# driver.find_element(By.XPATH,"//span[text()='×']").click()
#
# payments = driver.find_elements(By.XPATH,"//div[@class='title']")
# print(len(payments))
#
# for payment in payments:
#     print(payment.text)
#     if payment.text == "Pay with  UPI/Cards/Net Banking " :
#         payment.click()
#         time.sleep(2)
#         break
#


