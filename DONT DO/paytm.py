import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)

# Open paytm
driver.get("https://paytm.com/")

#Ticket booking
movie = wait.until(EC.visibility_of_element_located((By.XPATH,"//li[text()='Ticket Booking']")))
movie.click()

# Clicking movie ticket and switching to another window
driver.find_element(By.XPATH,"//a[text()='Movie Tickets']").click()
driver.switch_to.window(driver.window_handles[1])

# enter Location
driver.find_element(By.CLASS_NAME,"AnimatedSearchBar_animInput__iuqxe").send_keys("kakinada")
driver.find_element(By.XPATH,"//div/div[text()='Kakinada']").click()

# closing the popup
driver.find_element(By.CLASS_NAME,"PageBlockWidget_closeBtn__MdHIU").click()
wait.until(EC.visibility_of_element_located((By.XPATH,"//span[text()='View all 11 Movies']"))).click()

# searching movie
movies = driver.find_elements(By.XPATH,"//div[contains(@class,'DesktopRunningMovie_movTitle__Q1pOY')]")
print(len(movies))

for movie in movies:
    if movie.text == "#Single":
        movie.click()
        break

# clicking premium
driver.find_element(By.XPATH,"//span[text()='Premium Seats']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//span[text()='Premium Seats']").click()

# clicking show time
timings = driver.find_elements(By.XPATH,"//div[@class='greenCol MovieSessionsListingDesktop_time__r6FAI']")

for timing in timings:
    if timing.text == "09:30 PM" :
        timing.click()
        break

driver.find_element(By.XPATH,"//span[text()='E8']").click()
driver.find_element(By.XPATH,"//span[text()='E7']").click()
time.sleep(3)


driver.find_element(By.XPATH,"//button[text()='Book ']").click()
time.sleep(3)

# driver.find_element(By.ID,"email_mobile_login").send_keys("vdfdfd@gmail.com")
# driver.find_element(By.ID,"password_login").send_keys("fdfdfdfdffddf")
# driver.find_element(By.CLASS_NAME,"_1ugqt-nYs-aylKgBgMUzUL  ").click()
time.sleep(4)
driver.quit()
