import HtmlTestRunner
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time

class suite(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\driverchrome\chromedriver.exe")
        
    def test_busqueda(self):
        driver = self.driver
        driver.get("http://www.google.com")
        busqueda = driver.find_element_by_name("q")
        busqueda.send_keys("selenium")
        busqueda.submit()
        time.sleep(2)

    def test_usando_toggle(self):
        driver = self.driver
        driver.get("https://www.w3schools.com/howto/howto_css_switch.asp")
        time.sleep(2)
        toggle = driver.find_element_by_xpath("//*[@id='main']/label[3]/div")
        toggle.click()
        time.sleep(2)
        toggle.click()
        time.sleep(2)

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

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Resultados del testplan xd'))