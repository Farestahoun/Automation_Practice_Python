import unittest
from pages.Flights import Flights
import pytest
from ddt import ddt, data, unpack


@pytest.mark.usefixtures("oneTimeSetUp", "setUp_main", "browser", "osType")
class SelectFlightDates(unittest.TestCase):

    def setUp(self):
        self.tests_Dates = Flights(self.driver)

    def testSearchFlights(self):
        self.tests_Dates.get_flights()
        self.tests_Dates.click_flights()
        self.tests_Dates.get_dept_dates()
        self.tests_Dates.click_dept_dates()
        self.tests_Dates.get_dept_calendar()
        self.tests_Dates.select_dept_date()
        self.tests_Dates.take_screenshots()
