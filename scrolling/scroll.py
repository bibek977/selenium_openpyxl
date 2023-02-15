import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://mdbootstrap.com/docs/standard/methods/lazy-loading/")

driver.maximize_window()

driver.execute_script("window.scrollTo(0,2900)")
time.sleep(3)
img_src = driver.find_element(By.XPATH,"//img[@class='img-fluid mb-3']").get_attribute('src')
time.sleep(3)

# img_location = driver.find_element(By.XPATH,"//img[@class='img-fluid mb-3']")
# time.sleep(3)
# driver.execute_script("arguments[0].scrollIntoView();", img_location)
# time.sleep(3)
# img_src_2 = driver.find_element(By.XPATH,"//img[@class='img-fluid mb-3']").get_attribute('src')


# y = 1000
# for step in range(0,5):
#     driver.execute_script("window.scrollTo(0, "+str(y)+")")
#     y += 1000  
#     time.sleep(1)


print(img_src)
# print(img_src_2)