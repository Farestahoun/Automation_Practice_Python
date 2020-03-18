# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support import wait
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.common.exceptions import *
# #from Basics.RunChrome import PropertyManager
# from datetime import datetime
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver import ActionChains
# import logging
# import logging.config
#
#
# class LocatorElements:
#
#     def __init__(self, driver):
#         self.driver = driver
#
#     def find_loc(self, identifier, identifier_value):
#         web_element = None
#         wait_driver = WebDriverWait(self.driver, 10, poll_frequency=1, ignored_exceptions=[NoSuchAttributeException,
#                                                                                            NoSuchElementException,
#                                                                                            ElementNotVisibleException])
#         try:
#             if identifier == "XPATH":
#                 web_element = wait_driver.until(expected_conditions.element_to_be_clickable((By.XPATH, identifier_value)))
#             elif identifier == "ID":
#                 web_element = self.driver.find_element(By.XPATH, identifier_value)
#             elif identifier == "TAG_NAME":
#                 web_element = self.driver.find_element(By.TAG_NAME, identifier_value)
#             elif identifier == "CLASS_NAME":
#                 web_element = self.driver.find_element(By.CLASS_NAME, identifier_value)
#             elif identifier == "CSS_SELECTOR":
#                 web_element = self.driver.find_element(By.CSS_SELECTOR, identifier_value)
#             elif identifier == "LINK_TEXT":
#                 web_element = self.driver.find_element(By.LINK_TEXT, identifier_value)
#             elif identifier == "NAME":
#                 web_element = self.driver.find_element(By.NAME, identifier_value)
#             elif identifier == "PARTIAL_LINK_TEXT":
#                 web_element = self.driver.find_element(By.PARTIAL_LINK_TEXT, identifier_value)
#
#             if web_element is not None:
#                 return web_element
#             else:
#                 return None
#         except:
#             print("Locator doesn't exist")
#
#     def page_screenshots(self):
#         try:
#             self.driver.save_screenshot(str(datetime.now())+".png")
#         except NotADirectoryError:
#             print("Not a valid Directory or file extension")
#
#     def find_element_js_exec(self, js_command, scrollable_element=None):
#         web_element_js = self.driver.execute_script(js_command)
#         return web_element_js
#
#     def always_switch(self, type_of_switch):
#         if type_of_switch == "window":
#             parent_handle = self.driver.current_window_handle
#             handles = self.driver.window_handles
#             for handle in handles:
#                 if handle not in parent_handle:
#                     self.driver.switch_to.window(handle)
#                     print("Switched successfully to New Window")
#         else:
#             self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
#             print("Switched Successfully to New Tab")
#
#     def find_element_mouse(self, mouse_element):
#         actions = ActionChains(self.driver)
#         actions.move_to_element(mouse_element).perform()
#         self.driver.implicitly_wait(3)
#
#     def drag_drop(self, from_element, to_element):
#         actions = ActionChains(self.driver)
#         actions.drag_and_drop(from_element, to_element).perform()
#
#     def custom_logging(self, log_level=None):
#         #logging.basicConfig(filename="Debug.log", level=logging.DEBUG)
#         #
#         logging.basicConfig(filename="Formatted_log.log", format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
#                             datefmt="%m/%d/%Y %I:%M:%S %p", level=logging.NOTSET)
#         #return logger
#
#
# # test = PropertyManager("Chrome", "C:\\Users\\sedky\\PycharmProjects\\Automation_Practice\\Basics\\libs\\chromedriver.exe")
# # test.open_browser("https://www.expedia.com/")
# # ob = LocatorElements(test.driver)
# # ob.custom_logging()
# # element = ob.find_loc("XPATH", "//span[contains(text(),'Flights')]")
# # element.click()
# # #logging_val.debug(element.click())
# # element_depar = ob.find_loc("XPATH", "//label[@for='flight-departing-hp-flight']")
# # element_depar.click()
# # #logging_val.debug(element_depar.click())
# # mon_year = datetime.now().strftime('%h') + " " + datetime.now().strftime('%Y')
# # element_cal = ob.find_loc("XPATH", "//caption[contains(text(),'"+mon_year+"')]//..//*[@data-day='30']")
# # print(element_cal.text)
# # element_cal.click()
# # print(mon_year)
# # ob.page_screenshots()
# # element_by_js = ob.find_element_js_exec("return document.getElementById('tab-activity-tab-hp')")
# # element_by_js.click()
# # print(type(element_by_js))
# # ob.page_screenshots()
# # view_more_element = ob.find_loc("XPATH", "//a[contains(@onclick,'xxshowMoreCards(9)')]")
# # #ob.find_element_js_exec("arguments[0].scrollIntoView();", view_more_element)
# # ob.find_element_mouse(view_more_element)
# # ob.driver.close()
# # ob.custom_logging()
