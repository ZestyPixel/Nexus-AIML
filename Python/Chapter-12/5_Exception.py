try: 
    a = int(input("Enter a number: "))
except ValueError as e:
    print("Invalid input, please enter a valid number.")
    print(e)