import os
import requests
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
media_element = driver.find_element(By.XPATH,'//*[@id="nav"]/li[10]/a')

action = ActionChains(driver)
# Move the cursor to the element
action.move_to_element(media_element).perform()
time.sleep(4)

press_releases = driver.find_element(By.XPATH,"/html/body/nav/div/div/div/ul/li[10]/ul/li/a")
press_releases.click()
time.sleep(4)

more_info = driver.find_element(By.XPATH, '//*[@id="fontSize"]/div/div/div[3]/div[2]/div[1]/div/div/div/div/div/div/div/div/div/p/b/a')
more_info.click()
time.sleep(4)

photo_gallery = driver.find_element(By.XPATH, '//*[@id="block-block-88"]/ul/li[2]/strong/a')
photo_gallery.click()
time.sleep(4)


photo_gallery_window = driver.window_handles[1]
driver.switch_to.window(photo_gallery_window)


# Create a folder
folder_name = "photo_gallery"
download_dir = os.path.join(os.getcwd(), folder_name)
os.makedirs(download_dir, exist_ok=True)

table = driver.find_element(By.XPATH , '//*[@id="fontSize"]/div/div/div[3]/div[2]/div[1]/div/div/div[2]/div[2]/table')

# Get all rows of the table
rows = table.find_elements(By.TAG_NAME, 'tr')
count = 0
for row in rows:
    if count >= 10:
        break
    # Get all columns of the current row
    columns = row.find_elements(By.TAG_NAME, 'td')
    # Iterate over each column in the row
    for column in columns:
        if count >= 10:
            break
        try :
            # Access the text content of the column
            img_element = column.find_element(By.TAG_NAME,'img')
            img_src = img_element.get_attribute('src')
            img_title = img_element.get_attribute('title')
            print("Downloading image {}", img_title)
            # Use requests to get the image data
            response = requests.get(img_src)
            # Check if the request was successful
            if response.status_code == 200:
                # Save the image data to a file
                with open(f"{folder_name}/{img_title}.jpg", "wb") as f:
                    f.write(response.content)
                print("Image downloaded successfully.")
                count += 1
            else:
                print("Failed to download the image.")
            time.sleep(5)
        except :
            print("Failed to download the image.")
# Close the browser
driver.quit()

