# 2. Write a class “Calculator” capable of finding square, cube and square root of a\ number.
# 4. Add a static method in problem 2, to greet the user with hello.

import math
class Calculator:
    def __init__(self, number):
        self.number = number

    def square(self):
        return self.number ** 2

    def cube(self):
        return self.number ** 3

    def square_root(self):
        return math.sqrt(self.number)

    @staticmethod
    def greet():
        print("Hello, welcome to the Calculator!")

calc = Calculator(4)
print("Square:", calc.square())
print("Cube:", calc.cube())
print("Square Root:", calc.square_root())
Calculator.greet()