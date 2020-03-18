from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class PropertyManager:
    __instance = None

    def __init__(self, driver_type, executable_path):
        if PropertyManager.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            PropertyManager.__instance = self
        if driver_type == "Chrome":
            self.driver = webdriver.Chrome(executable_path)
        elif driver_type == "FF":
            self.driver = webdriver.Firefox(executable_path)
        elif driver_type == "Safari":
            self.driver = webdriver.Safari(executable_path)
        else:
            print("Undefined WebDriver")

    def open_browser(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    @staticmethod
    def getInstance():
        """ Static access method. """
        if PropertyManager.__instance is None:
            PropertyManager()
        return PropertyManager.__instance

    def insert_text(self, text):
        txt_name = self.driver.find_element_by_xpath("//input[contains(@placeholder,'Name')]")
        txt_name.send_keys(text)

    def introduce_s_four(self):
        element = self.driver.find_element(By.XPATH, "//a[@id='opentab']")
        #element.click()
        #self.driver.switch_to.window(self.driver.window_handles[1])
        #search_course = self.driver.find_element_by_xpath("//input[contains(@id,'search-co')]")
        #search_course.send_keys("Python")#
        list_of_cars = self.driver.find_elements(By.XPATH, "//legend[contains(text(),'Radio')]/..//label")
        # for car in list_of_cars:
        #     print(car.get_attribute("for"))
        #     car.screenshot("test_file.png")
        table_access = self.driver.find_elements(By.XPATH, "//table[contains(@id,'product')]//tbody//tr//*")
        for th in table_access:
            print(th.tag_name)
            if th.tag_name == "th":
                print("These are Table Headers", th.text)
            elif th.tag_name == "td":
                print("These are Table Values", th.text)
            else:
                print("No values ...")

        car_dd = Select(self.driver.find_element(By.XPATH, "//select[contains(@id,'car')]"))
        car_dd.select_by_index(2)
        print(car_dd.first_selected_option.text)


# P = PropertyManager("Chrome", "C:\\Users\\sedky\\PycharmProjects\\Automation_Practice\\Basics\\libs\\chromedriver.exe")
# P.open_browser("https://learn.letskodeit.com/p/practice")
# P.insert_text("Hello_Python")
# P.introduce_s_four()
