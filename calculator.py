"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *



# Your code goes here
while True:
    user_input = raw_input('>')
    token = user_input.split()

    num = token[1:]

    def calc_math(operand, math_function):
     
        if token[0] == operand:
            print math_function

    calc_math("+", add(float(num[0]), float(num[1])))

    calc_math("-", subtract(float(num[0]), float(num[1])))

    calc_math("*", multiply(float(num[0]), float(num[1])))

    calc_math("/", divide(float(num[0]), float(num[1])))

    calc_math("square", square(float(num[0])))

    calc_math("cube", cube(float(num[0])))

    calc_math("mod", mod(float(num[0]), float(num[1])))

    calc_math("power", power(float(num[0]), float(num[1])))


