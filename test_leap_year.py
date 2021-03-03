# CS362 test_leap_year.py
# Alex Young
# 3/3/2021
# Run this file using python3 test_leap_year.py or just pytest
# This program tests if the Leap Year program works correctly

import unittest
import leap_year

class TestLeapYear(unittest.TestCase):
    def test_1(self):
        self.assertEqual(leap_year.run(1), "is not a leap year")
        self.assertEqual(leap_year.run(2002), "is not a leap year")
    def test_2(self):
        self.assertEqual(leap_year.run(4), "is a leap year")
        self.assertEqual(leap_year.run(8), "is a leap year")
    def test_3(self):
        self.assertEqual(leap_year.run(100), "is not a leap year")
        self.assertEqual(leap_year.run(2300), "is not a leap year")
    def test_4(self):
        self.assertEqual(leap_year.run(400), "is a leap year")
        self.assertEqual(leap_year.run(2800), "is a leap year")
    def test_5(self):
        self.assertEqual(leap_year.run("0"), "invalid input")

if __name__ == '__main__':
    unittest.main(verbosity=2)