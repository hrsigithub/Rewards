from selenium import webdriver
from selenium.webdriver.safari.service import Service as SafariService
import time

service = SafariService()
driver = webdriver.Safari(service=service)

# User-Agentを偽装する
driver.execute_script("navigator.__defineGetter__('userAgent', () => 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15');")


# サイトにアクセス
driver.get('https://rewards.bing.com')

time.sleep(10)

driver.quit()
