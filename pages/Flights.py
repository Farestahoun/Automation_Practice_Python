from base.PManager import PManager
from datetime import datetime
from ddt import ddt, data, unpack


class Flights(PManager):

    def __init__(self, driver):
        super(PManager, self).__init__()
        self.driver = driver

    def get_flights(self):
        element = self.find_loc("XPATH", "//span[contains(text(),'Flights')]")
        return element

    def click_flights(self):
        self.get_flights().click()

    def get_dept_dates(self):
        element_depar = self.find_loc("XPATH", "//label[@for='flight-departing-hp-flight']")
        return element_depar

    def click_dept_dates(self):
        self.get_dept_dates().click()

    def get_dept_calendar(self):
        mon_year = datetime.now().strftime('%h') + " " + datetime.now().strftime('%Y')
        element_cal = self.find_loc("XPATH", "//caption[contains(text(),'"+mon_year+"')]//..//*[@data-day='30']")
        return element_cal

    def select_dept_date(self):
        self.get_dept_calendar().click()

    def take_screenshots(self):
        self.page_screenshots()

#element = ob.find_loc("XPATH", "//span[contains(text(),'Flights')]")
# element.click()
# #logging_val.debug(element.click())
# element_depar = ob.find_loc("XPATH", "//label[@for='flight-departing-hp-flight']")
# element_depar.click()
# #logging_val.debug(element_depar.click())
# mon_year = datetime.now().strftime('%h') + " " + datetime.now().strftime('%Y')
# element_cal = ob.find_loc("XPATH", "//caption[contains(text(),'"+mon_year+"')]//..//*[@data-day='30']")
# print(element_cal.text)
# element_cal.click()
# print(mon_year)
# ob.page_screenshots()
# element_by_js = ob.find_element_js_exec("return document.getElementById('tab-activity-tab-hp')")
# element_by_js.click()
# print(type(element_by_js))
# ob.page_screenshots()
# view_more_element = ob.find_loc("XPATH", "//a[contains(@onclick,'xxshowMoreCards(9)')]")
# #ob.find_element_js_exec("arguments[0].scrollIntoView();", view_more_element)
# ob.find_element_mouse(view_more_element)
# ob.driver.close()
# ob.custom_logging()
