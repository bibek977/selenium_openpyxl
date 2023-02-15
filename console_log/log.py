from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

dc = DesiredCapabilities.CHROME
dc['goog:loggingPrefs'] = { 'browser':'ALL' }

message = []

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), desired_capabilities=dc)
driver.get("https://www.tutorialspoint.com/getting-console-log-output-from-chrome-with-selenium-python-api-bindings")

logs = driver.get_log('browser')

for data in logs:
    # print(data)

    if data['level'] == 'SEVERE':
        print(data['message'])

        message.append(data['message'])

print(message)

driver.quit()