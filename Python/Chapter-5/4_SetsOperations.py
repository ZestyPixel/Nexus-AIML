s = {1,8,2,3}

print(len(s))
s.remove(8)
print(s.pop()) #Removes random num from the set
s.clear() #Empties set
s.union({8,11}) #Returns new set with all elements from both sets
s.intersection({8,11}) #Returns set with items that are present in both sets

