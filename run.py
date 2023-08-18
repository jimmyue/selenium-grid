import time
from selenium import webdriver

options = webdriver.ChromeOptions() # ChromeOptions / EdgeOptions / FirefoxOptions
driver = webdriver.Remote(command_executor='http://10.10.10.71:4444/wd/hub', options=options)
driver.implicitly_wait(3)        #隐性等待
driver.get('https://www.baidu.com')
driver.maximize_window()         #浏览器全屏
print(driver.title)
time.sleep(30)
driver.quit()
