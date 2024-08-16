from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://nextdoor.co.uk/news_feed")
options = webdriver.ChromeOptions() #newly added 
options.add_argument("--headless") #newly added 


time.sleep(3)
search_box = driver.find_element(By.ID, 'didomi-notice-agree-button')
search_box.send_keys(Keys.RETURN)
time.sleep(5)
search_box = driver.find_element(By.ID, 'google-button')
search_box.send_keys(Keys.RETURN)
time.sleep(35)

# You can now interact with the search results using Selenium
# For example, you could click on a specific link or extract information

# Close the browser
driver.quit()