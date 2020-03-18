import unittest
from Basics.RunChrome import PropertyManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from Basics.RunChrome import PropertyManager
from datetime import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import logging
import logging.config
from Basics.libs.Generic_locator import LocatorElements
import pytest


@pytest.mark.usefixtures("PropertyManager", "")
class TestCase(unittest.TestCase):

    def setUp(self) -> None:
        init = PropertyManager("Chrome", "C:\\Users\\sedky\\PycharmProjects\\Automation_Practice\\Basics\\libs\\chromedriver.exe")
        init.open_browser("https://www.expedia.com/")
        self.driver = init.driver

    def testFlights(self):
        locate_elements = LocatorElements(self.driver)
        locators_class = locate_elements.find_loc("XPATH", "//span[contains(text(),'Flights')]")
        locators_class.click()

    def testCalendar(self):
        locate_elements = LocatorElements(self.driver)
        locators_class = locate_elements.find_loc("XPATH", "//span[contains(text(),'Flights')]")
        locators_class.click()
        element_depar = locate_elements.find_loc("XPATH", "//label[@for='flight-departing-hp-flight']")
        element_depar.click()
        mon_year = datetime.now().strftime('%h') + " " + datetime.now().strftime('%Y')
        element_cal = locate_elements.find_loc("XPATH", "//caption[contains(text(),'"+mon_year+"')]//..//*[@data-day='30']")
        print(element_cal.text)
        element_cal.click()

    def tearDown(self) -> None:
        self.driver.close()
