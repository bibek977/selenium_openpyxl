import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

workbook = openpyxl.Workbook()
sheet = workbook.active

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

sheet.title = "Demo Sheet"

table_row = driver.find_elements(By.XPATH,"//div[@class='tableFixHead']//tbody/tr")
table_head_column = driver.find_elements(By.XPATH,"//table[@id='product']//thead/tr/th")

j = 1

for data in table_row:
    
    i = 1

    for item in table_head_column:

        sheet.cell(j, i).value = driver.find_element(By.XPATH,"//div[@class='tableFixHead']//tbody/tr["+str(j)+"]/td["+str(i)+"]").text

        i = i+1

    j += 1

workbook.save("Excel_sheets/Tuto_1.xlsx")