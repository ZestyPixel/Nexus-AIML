l = [1, 2, 3, 4, 5]

square = lambda x: x * x

sq_list = map(square, l) # Map is used to apply a function to all items in an iterable.
print(list(sq_list))

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def even(n):
    if (n % 2 == 0):
        return True
    return False

even_list = filter(even, l) # Filter is used to filter items out of an iterable based on a function that returns True or False.
print(list(even_list))


def add(x, y):
    return x + y

from functools import reduce
print(reduce(add, l)) # Reduce is used to apply a function to the items of an iterable, from left to right, so as to reduce the iterable to a single value.
