import unittest
from tests.Flights_test import FlightTest
from tests.SelectFlightsDates import SelectFlightDates

TestCase_I = unittest.TestLoader().loadTestsFromTestCase(FlightTest)
TestCase_II = unittest.TestLoader().loadTestsFromTestCase(SelectFlightDates)

Smoke_Test = unittest.TestSuite([TestCase_I, TestCase_II])

unittest.TextTestRunner(verbosity=2).run(Smoke_Test)
