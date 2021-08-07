from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\driverchrome\chromedriver.exe")
driver.get("http://google.com")
driver.close()