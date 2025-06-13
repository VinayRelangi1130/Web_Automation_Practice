import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.myntra.com/")
actions = ActionChains(driver)

profile = driver.find_element(By.XPATH,"//span[text()='Profile']")
actions.move_to_element(profile).perform()

men = driver.find_element(By.XPATH,"//div[@class='desktop-navLink']/a[text()='Men']")
actions.move_to_element(men).perform()

t_shirts = driver.find_element(By.XPATH,"//a[@data-reactid=31]")
t_shirts.click()
time.sleep(2)

categor = driver.find_element(By.XPATH,"//label[text()='Tshirts']")
categor.click()
time.sleep(2)

brand = driver.find_element(By.XPATH,"//label[text()='Tommy Hilfiger']")
brand.click()
time.sleep(2)

color = driver.find_element(By.XPATH,"//label[text()='Blue']")
color.click()
time.sleep(2)

discount = driver.find_element(By.XPATH,"//label[text()='10% and above']")
discount.click()
time.sleep(3)

pages = driver.find_element(By.XPATH,"//li[text()='Next']")
driver.execute_script("arguments[0].scrollIntoView(true);", pages)
time.sleep(2)

next_btn = driver.find_element(By.XPATH,"//li[text()='Next']")
driver.execute_script("arguments[0].click();", next_btn)

sorting = driver.find_element(By.XPATH,"//div[text()='Sort by : ']")
actions.move_to_element(sorting).perform()
time.sleep(2)

select_shirt = driver.find_element(By.XPATH,"//h4[text()='Pure Cotton Printed T-shirt']")
select_shirt.click()
time.sleep(2)

driver.switch_to.window(driver.window_handles[1])

pincode = driver.find_element(By.XPATH,"//input[@name='pincode']")
pincode.send_keys("533002")
pincode.send_keys(Keys.ENTER)
time.sleep(1)

size_chart = driver.find_element(By.XPATH,"//button[text()='Size Chart']")
size_chart.click()
time.sleep(1)

large_size_click = driver.find_element(By.XPATH,"//td[text()='42.0']")
driver.execute_script("arguments[0].click();", large_size_click)
time.sleep(1)

close_btn = driver.find_element(By.XPATH,"//button[@class='sizeChartWeb-close sizeChartWeb-button']")
close_btn.click()

driver.find_element(By.XPATH,"//p[text()='L']").click()

add_to_bag = driver.find_element(By.XPATH,"//div[text()='ADD TO BAG']")
add_to_bag.click()
time.sleep(2)

go_to_bag = driver.find_element(By.XPATH,"//span[text()='GO TO BAG']")
go_to_bag.click()
time.sleep(2)

address = driver.find_element(By.XPATH,"//div[text()='CHANGE ADDRESS']")
address.click()
time.sleep(2)

re_enter_pincode = driver.find_element(By.XPATH,"//input[@id='pincode']")
time.sleep(2)
re_enter_pincode.send_keys("533006")
time.sleep(1)

check_btn = driver.find_element(By.XPATH,"//div[text()='CHECK']")
check_btn.click()

apply_coupon = driver.find_element(By.XPATH,"//div[text()='APPLY']")
apply_coupon.click()
time.sleep(2)

enter_coupon = driver.find_element(By.XPATH,"//input[@id='coupon-input-field']")
enter_coupon.send_keys("dfdfdfdfdf")
time.sleep(2)
driver.find_element(By.XPATH,"//div[text()='CHECK']").click()

cancel_btn = driver.find_element(By.CLASS_NAME,"modal-base-cancelIcon")
cancel_btn.click()
time.sleep(1)

place_order = driver.find_element(By.XPATH,"//div[text()='PLACE ORDER']")
place_order.click()

time.sleep(2)
driver.quit()