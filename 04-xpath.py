import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class usando_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\driverchrome\chromedriver.exe")

    def test_buscarPorXpath(self):
        driver = self.driver
        driver.get("http://www.google.com")
        time.sleep(3)
        buscarPorXpath = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
        time.sleep(3)
        buscarPorXpath.send_keys("selenium", Keys.ARROW_DOWN)
        time.sleep(3)
    
    def tearDown(self):
        self.driver.close
    
if __name__ == "__main__":
    unittest.main()

#xpath es una estructura de "carpetas", objetos, etc.
#xpath relativo //*[@id="input"]
#xpath absoluto