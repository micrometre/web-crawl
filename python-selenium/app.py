import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get("https://nextdoor.co.uk/news_feed")

#search = browser.find_element(By.NAME, "q")
#search.send_keys("selenium")
#search.send_keys(Keys.RETURN) # hit return after you enter search text
time.sleep(25) # sleep for 5 seconds so you can see the results
browser.quit()