a = int(input("Enter a number: "))
b = int(input("Enter second number: "))

try:
    c = a / b
    print(f"The result of {a} divided by {b} is {c}")
except ZeroDivisionError:
    print("Infinite (division by zero is not allowed)")