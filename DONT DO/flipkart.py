from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)

driver.get("https://www.flipkart.com")
print(driver.title)

# Search for "iphone 16"
search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
search_box.send_keys("iphone 16")
search_box.send_keys(Keys.ENTER)

# Click first search result
product_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='container']/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a")))
product_link.click()

# Switch to product tab
wait.until(EC.number_of_windows_to_be(2))
driver.switch_to.window(driver.window_handles[1])

# Click "Add to cart"
add_to_cart = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Add to cart']")))
add_to_cart.click()

# Click "+" to increase quantity
plus_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='+']")))
plus_button.click()

# Click "Place Order"
place_order = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Place Order']")))
place_order.click()








