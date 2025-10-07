a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

if b == 0:
    raise ValueError("The value of b cannot be zero")
else:
    print(a/b)