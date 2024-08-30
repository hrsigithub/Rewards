from selenium import webdriver
import time

driver = webdriver.Safari()

target = 'https://rewards.bing.com'

driver.get(target)


time.sleep(10)

driver.quit()
