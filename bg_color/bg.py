from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.color import Color

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

rgb = driver.find_element(By.XPATH,"//button[normalize-space()='Home']").value_of_css_property('background-color')
btn_bg_color = Color.from_string(rgb).hex

print(btn_bg_color)