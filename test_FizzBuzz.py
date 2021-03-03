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
        self.assertEqual(FizzBuzz.run(2), 2)
    def test2(self):
        self.assertEqual(FizzBuzz.run(3), "Fizz")
        self.assertEqual(FizzBuzz.run(6), "Fizz")
    def test3(self):
        self.assertEqual(FizzBuzz.run(5), "Buzz")
        self.assertEqual(FizzBuzz.run(10), "Buzz")
    def test4(self):
        self.assertEqual(FizzBuzz.run(15), "FizzBuzz")
        self.assertEqual(FizzBuzz.run(30), "FizzBuzz")

if __name__ == '__main__':
    unittest.main(verbosity=2)