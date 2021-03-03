# CS362 test_FizzBuzz.py
# Alex Young
# 3/2/2021
# Run this file using python3 test_FizzBuzz.py or just pytest
# This program tests if the FizzBuzz program works correctly

import unittest
import FizzBuzz

class TestFizzBuzz(unittest.TestCase):
    def test1(self):
        self.assertEqual(FizzBuzz.run(1), 1)

if __name__ == '__main__':
    unittest.main(verbosity=2)