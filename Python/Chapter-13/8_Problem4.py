l = [5, 12, 15, 22, 25, 30, 33, 40, 45, 50]
def divisible_by_5(n):
    if (n % 5 == 0):
        return True
    return False

divisible_by_5_list = filter(divisible_by_5, l)
print(list(divisible_by_5_list))