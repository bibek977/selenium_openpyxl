from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

dc = DesiredCapabilities.CHROME
dc['goog:loggingPrefs'] = { 'performance':'ALL' }

network = []

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), desired_capabilities=dc)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# logs = driver.get_log('performance')

# for data in logs:
#     # print(data)

#     if data['level'] == 'SEVERE':
#         print(data['message'])

#         message.append(data['message'])

# print(message)

for request in driver.requests:
    if request.response.status_code >=200:
        network.append(request.url)

print(network)

driver.quit()