from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r"C:\driverchrome\chromedriver.exe")
driver.get("http://www.w3schools.com/")
time.sleep(3)
encontrar_link = driver.find_element_by_link_text('Learn PHP')
encontrar_link.click()