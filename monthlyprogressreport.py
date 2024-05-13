import os
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By

paths = r"C:\Users\chand\Downloads\chromedriver-win32\chromedriver-win32\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(paths)
chrome_options=Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
time.sleep(3)
driver.get("https://labour.gov.in/")

original_window = driver.current_window_handle
driver.maximize_window()
time.sleep(3)
documentElement = driver.find_element(By.XPATH,'//*[@id="nav"]/li[7]')

action = ActionChains(driver)

# Move the cursor to the element
action.move_to_element(documentElement).perform()

# firstwindow = driver.window_handles[0]
# driver.switch_to.window(firstwindow)
time.sleep(4)

monthlyprogressreport = driver.find_element(By.XPATH,"/html/body/nav/div/div/div/ul/li[7]/ul/li[2]")
monthlyprogressreport.click()

time.sleep(3)

download_element = driver.find_element(By.XPATH, "/html/body/section[3]/div/div/div[3]/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[2]/div[2]/table/tbody/tr[2]/td[2]/a")
download_element.click()

time.sleep(3)
alert = driver.switch_to.alert
alert.accept()



# firstwindow = driver.window_handles[1]
# driver.switch_to.window(firstwindow)
# time.sleep(3)
# driver.maximize_window()