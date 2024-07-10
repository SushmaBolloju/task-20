import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.cowin.gov.in/")
original_window = driver.current_window_handle
driver.maximize_window()
time.sleep(3)
faq = driver.find_element(By.XPATH,"/html/body/app-root/app-header/header/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[4]/a")
faq.click()
firstwindow = driver.window_handles[0]
driver.switch_to.window(firstwindow)
# firstwindow=driver.title
# print(firstwindow)
time.sleep(3)
driver.maximize_window()
displayedelement=driver.find_element(By.LINK_TEXT,"FAQ").is_displayed()
print(driver.find_element(By.XPATH,"/html/body/app-root/app-header/header/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[4]/a").text)
time.sleep(5)

partners = driver.find_element(By.XPATH,"/html/body/app-root/app-header/header/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[5]/a")
partners.click()
secondwindow = driver.window_handles[1]
driver.switch_to.window(secondwindow)

time.sleep(3)
driver.maximize_window()
displayedelement=driver.find_element(By.LINK_TEXT,"PARTNERS").is_displayed()
print(driver.find_element(By.XPATH,"/html/body/app-root/app-header/header/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[5]/a").text)
time.sleep(2)


# return all handles value of open browser window
handles = driver.window_handles

for i in handles:
	driver.switch_to.window(i)
	if driver.current_url.__contains__("faq") or driver.current_url.__contains__("our-partner"):
		driver.close()
	time.sleep(2)







