import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

class usando_unittest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\driverchrome\chromedriver.exe")
    
    def test_usando_select(self):
        driver = self.driver
        driver.get("https://www.w3schools.com/howto/howto_custom_select.asp")
        time.sleep(2)
        select = driver.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/select")
        opcion = select.find_elements_by_tag_name("option")
        time.sleep(2)

        for option in opcion:
            print("Los valores son: " + option.get_attribute("value"))
            option.click()
            time.sleep(1)
        
        seleccionar = Select(driver.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/select"))
        seleccionar.select_by_value("10")
        time.sleep(2)


if __name__ == '__main__':
    unittest.main()