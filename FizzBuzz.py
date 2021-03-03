# CS362 HW 7
# Alex Young
# 3/3/2021
# Run this file using python3 FizzBuzz.py
# This program prints numbers from 1 to 100 with
# multiples of 3 printing "Fizz", multiples of 5
# printing "Buzz" and multiples of both "FizzBuzz"

def run(x):
    if (x < 1 or x > 100):
        return("Out of Bounds")
    if (x % 3 == 0 and x % 5 == 0):
        return "FizzBuzz"
    elif (x % 3 == 0):
        return "Fizz"
    elif (x % 5 == 0):
        return "Buzz"
    else:
        return x