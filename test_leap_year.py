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


if __name__ == '__main__':
    unittest.main(verbosity=2)