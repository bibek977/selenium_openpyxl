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

# table_data = driver.find_elements(By.XPATH,"//div[@class='tableFixHead']/table[@id='product']/tbody/tr")
table_row = driver.find_elements(By.XPATH,"//div[@class='tableFixHead']//tbody/tr")
i = 1
for data in table_row:
    table_column = driver.find_elements(By.XPATH,f"//div[@class='tableFixHead']//tbody/tr[{i}]/td")
    j = 1
    for item in table_column:
        sheet.cell(i, j).value = driver.find_element(By.XPATH,f"//div[@class='tableFixHead']//tbody/tr[{i}]/td[{j}]").text
        j +=1
    i += 1

workbook.save("Excel_sheets/Demo_1.xlsx")