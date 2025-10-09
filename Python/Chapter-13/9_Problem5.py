from functools import reduce
l = [5, 12, 15, 22, 25, 30, 33, 40, 45, 50]
def maximum(x, y):
    if (x > y):
        return x
    return y
print(reduce(maximum, l))