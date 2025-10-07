l = [101, 202, 303, 404, 505, 606, 707, 808, 909]
for index, value in enumerate(l):
    if index in (2, 4, 6):
        print(f"Element at index {index} is {value}")