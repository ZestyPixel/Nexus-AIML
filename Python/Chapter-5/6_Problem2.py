# Program to input 8 numbers and display unique numbers

numbers = set()

print("Enter 8 numbers:")

for i in range(8):
    num = int(input(f"Number {i+1}: "))
    numbers.add(num)
    
print("\nAll unique numbers are:")
for n in numbers:
    print(n)
