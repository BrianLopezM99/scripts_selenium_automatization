from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r"C:\driverchrome\chromedriver.exe")
driver.get("http://www.w3schools.com/html/default.asp")
time.sleep(2)
content = driver.find_element_by_css_selector('a.w3-blue')
content.click()
