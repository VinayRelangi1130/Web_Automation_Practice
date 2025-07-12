from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
options = Options()
options.add_argument('--incognito')
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()

driver.get("https://in.bookmyshow.com/")
time.sleep(2)
driver.find_element(By.XPATH,"//span[text()='View All Cities']").click()
time.sleep(2)
city_list = []
wait = WebDriverWait(driver, 5)
''' Popup handle and assertions '''
try:
    cities = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//span[text()='Other Cities']//parent::div/ul/li/div")))

    for i in cities:
        city_list.append(i.text)

    assert len(city_list) > 0 , "City List is empty"
    print("Total cities : ", len(cities))

except Exception as e:
    print("Error",e)

print(city_list)

try:
    search = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search for your city']")))
    search.click()
    a = False
    for city in city_list:
        print(city)
        if city.strip().lower() == "kakinada" :
            search.clear()
            search.send_keys(city)
            time.sleep(2)
            search.send_keys(Keys.ENTER)
            time.sleep(5)
            print(city,"selected successfully")
            a = True
            break
    assert a, "Kakinada not listed "

except Exception as e:
    print("Error while selecting the city in the list",e)

print("all set")

movies = driver.find_element(By.XPATH,"//a[text()='Movies']")
movies.click()
time.sleep(2)

Movies_in_kakinada = driver.find_element(By.XPATH,"//h1[text()='Movies in Kakinada']")
driver.execute_script("arguments[0].click();", Movies_in_kakinada)

'''  Sorry, you have been blocked
  '''


























# driver.find_element(By.XPATH,"//a[text()='Movies']").click()
# time.sleep(2)
#
# movies = driver.find_elements(By.XPATH,"//div[@class='sc-7o7nez-0 elfplV']")
# print(len(movies))
#
# ''' movie name in list'''
# for movie in movies:
#     if movie.text == "Subham" :
#         movie.click()
#         break
#
#
# time.sleep(2)
# driver.quit()
