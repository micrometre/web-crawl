from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

username = "username"
password = "password"
driver = webdriver.Chrome()
driver.get("https://nextdoor.co.uk/news_feed")


time.sleep(3)
search_box = driver.find_element(By.ID, 'didomi-notice-agree-button')
search_box.send_keys(Keys.RETURN)
time.sleep(3)
driver.find_element("id", "id_email").send_keys(username)
driver.find_element("id", "id_password").send_keys(password)

time.sleep(13)
# You can now interact with the search results using Selenium
# For example, you could click on a specific link or extract information

# Close the browser
driver.quit()