import unittest
from pages.Flights import Flights
import pytest
from ddt import ddt, data, unpack


@pytest.mark.usefixtures("oneTimeSetUp", "setUp_main", "browser", "osType")
class FlightTest(unittest.TestCase):

    #@pytest.fixture()
    def setUp(self):
        self.tests = Flights(self.driver)

    def testLogin(self):
        element = self.tests.get_flights()
        element.click()
        #self.tests.click_flights()
        self.tests.get_dept_dates()
        self.tests.click_dept_dates()
        self.tests.get_dept_calendar()
        self.tests.select_dept_date()
        self.tests.take_screenshots()

