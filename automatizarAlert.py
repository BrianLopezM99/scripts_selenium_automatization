from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r"C:\driverchrome\chromedriver.exe")
driver.get('file:///D:/Documents/proyectospersonales/cursoselenium/index.html')
time.sleep(2)
alerta = driver.find_element_by_name('alert')
alerta.click()
time.sleep(2)
alerta = driver.switch_to_alert()
alerta.dismiss()
time.sleep(2)
driver.close()
