import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class usando_unittest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\driverchrome\chromedriver.exe")
    
    def test_changeWindow(self):
        driver = self.driver
        driver.get("http://www.google.com")
        time.sleep(3)
        driver.execute_script("window.open('');")
        time.sleep(3)
        driver.switch_to_window(driver.window_handles[1])
        driver.get("http://youtube.com")
        time.sleep(3)
        driver.switch_to_window(driver.window_handles[0])
        time.sleep(3)

if __name__ == "__main__":
    unittest.main()