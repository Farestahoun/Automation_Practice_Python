from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from datetime import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import logging
import logging.config
from traceback import print_stack
from base import custom_logger as general_log
import unittest
import pytest


class PManager:
    log = general_log.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver
        # if driver_type == "Chrome":
        #     self.driver = webdriver.Chrome(executable_path)
        # elif driver_type == "FF":
        #     self.driver = webdriver.Firefox(executable_path)
        # elif driver_type == "Safari":
        #     self.driver = webdriver.Safari(executable_path)
        # else:
        #     print("Undefined WebDriver")
        #     self.log.info("Driver Cannot be created", self.driver)

    def open_browser(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
        self.log.info("Driver Opened and Maximized on following URL", url)

    def insert_text(self, text):
        txt_name = None
        try:
            txt_name = self.driver.find_element_by_xpath("//input[contains(@placeholder,'Name')]")
            txt_name.send_keys(text)
        except:
            self.log.error("Cannot find element or cannot insert text to", txt_name)

    def find_loc(self, identifier, identifier_value):
        web_element = None
        wait_driver = WebDriverWait(self.driver, 10, poll_frequency=1, ignored_exceptions=[NoSuchAttributeException,
                                                                                           NoSuchElementException,
                                                                                           ElementNotVisibleException])
        try:
            if identifier == "XPATH":
                web_element = wait_driver.until(expected_conditions.element_to_be_clickable((By.XPATH, identifier_value)))
            elif identifier == "ID":
                web_element = self.driver.find_element(By.XPATH, identifier_value)
            elif identifier == "TAG_NAME":
                web_element = self.driver.find_element(By.TAG_NAME, identifier_value)
            elif identifier == "CLASS_NAME":
                web_element = self.driver.find_element(By.CLASS_NAME, identifier_value)
            elif identifier == "CSS_SELECTOR":
                web_element = self.driver.find_element(By.CSS_SELECTOR, identifier_value)
            elif identifier == "LINK_TEXT":
                web_element = self.driver.find_element(By.LINK_TEXT, identifier_value)
            elif identifier == "NAME":
                web_element = self.driver.find_element(By.NAME, identifier_value)
            elif identifier == "PARTIAL_LINK_TEXT":
                web_element = self.driver.find_element(By.PARTIAL_LINK_TEXT, identifier_value)

            if web_element is not None:
                return web_element
            else:
                return None
        except:
            print("Locator doesn't exist")
            self.log.error("Element doesn't exists")

    def page_screenshots(self):
        try:
            self.driver.save_screenshot(str(datetime.now())+".png")
        except NotADirectoryError:
            print("Not a valid Directory or file extension")
            self.log.error("Not a valid Directory or file extension")

    def find_element_js_exec(self, js_command, scrollable_element=None):
        web_element_js = self.driver.execute_script(js_command)
        if web_element_js is not None:
            self.log.info("JS Executed successfully")
        else:
            self.log.error("JS script have issues!")
        return web_element_js

    def always_switch(self, type_of_switch):
        if type_of_switch == "window":
            parent_handle = self.driver.current_window_handle
            handles = self.driver.window_handles
            for handle in handles:
                if handle not in parent_handle:
                    self.driver.switch_to.window(handle)
                    print("Switched successfully to New Window")
                    self.log.info("Switched successfully to New Window")
        else:
            self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
            print("Switched Successfully to New Tab")
            self.log.info("Switched Successfully to New Tab")

    def find_element_mouse(self, mouse_element):
        actions = ActionChains(self.driver)
        try:
            actions.move_to_element(mouse_element).perform()
            self.driver.implicitly_wait(3)
        except:
            self.log.error("Cannot perform action!")

    def drag_drop(self, from_element, to_element):
        try:
            actions = ActionChains(self.driver)
            actions.drag_and_drop(from_element, to_element).perform()
        except:
            self.log.error("Cannot drag and drop element !", from_element)

    def custom_logging(self, log_level=None):
        logging.basicConfig(filename="Formatted_log.log", format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                            datefmt="%m/%d/%Y %I:%M:%S %p", level=logging.NOTSET)

    def click_element(self, locator, locator_identifier):
        try:
            element_to_click = self.find_loc(locator, locator_identifier)
            element_to_click.click()
        except:
            self.log("Cannot click element")

    def is_element_displayed(self, locator, locator_identifier):
        try:
            element = self.find_loc(locator, locator_identifier)
            if element is not None:
                print("Element displayed successfully")
                self.log.info("Element displayed successfully")
            else:
                print("Element not displayed")
                self.log.error("Element displayed successfully")
        except:
            print("Element not displayed")
            self.log.error("Element displayed successfully")

    def pytest_add_option(self, parser):
        parser.addoption("--browser")
        parser.addoption("--osType", help="Type of operating system")

    @pytest.fixture(scope="session")
    def browser(self, request):
        return request.config.getoption("--browser")

    @pytest.fixture(scope="session")
    def osType(self, request):
        return request.config.getoption("--osType")
