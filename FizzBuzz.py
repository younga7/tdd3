# CS362 HW 7
# Alex Young
# 3/3/2021
# Run this file using python3 FizzBuzz.py
# This program prints numbers from 1 to 100 with
# multiples of 3 printing "Fizz", multiples of 5
# printing "Buzz" and multiples of both "FizzBuzz"

def run(x):
    if (x % 3 == 0):
        return "Fizz"
    else:
        return x