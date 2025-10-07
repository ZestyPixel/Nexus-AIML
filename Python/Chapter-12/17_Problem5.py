num = int(input("Enter a number: "))
multiplication_table = [num * i for i in range(1, 11)]
with open("Tables.txt", "w") as f:
    f.write(f"Table of {num}: {str(multiplication_table)}\n")