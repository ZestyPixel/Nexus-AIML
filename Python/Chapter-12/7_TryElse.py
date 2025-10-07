try: 
    a = int(input("Enter a number: "))
except ValueError as e:
    print("Invalid input, please enter a valid number.")
    print(e)
else:
    print(f"You entered a valid number: {a}") # This block will execute only if no exception occurs in the try block.