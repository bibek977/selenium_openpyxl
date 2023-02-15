from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://pythonbasics.org/selenium-cookies/")


# cookies = driver.get_cookies()
# for cookie in cookies:
#     print(cookie)

print(driver.get_cookie('_ga')['value'])
driver.quit()