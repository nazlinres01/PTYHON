"""
#web otomasyon kütüphanesi
from selenium import webdriver
import time
driver=webdriver.Chrome()
url="http://github.com"
driver.get(url)

time.sleep(3)#program 3 sn çalışır
driver.maximize_window()
#driver.save_screenshot("github.com-homepage.png")

url="http://github.com/sadikturan"
driver.get(url)

if "sadikturan" in driver.title:
    driver.save_screenshot("github-sadikturan.png")

time.sleep(3)
driver.back()

print(driver.title)
driver.close()

"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome()

url="http://github.com"
driver.get(url)

searchInput=driver.find_element_by_name("q")
time.sleep(1)
searchInput.send_keys("python")
time.sleep(2)
searchInput.send_keys(Keys.ENTER)
time.sleep(2)

    
driver.close()




