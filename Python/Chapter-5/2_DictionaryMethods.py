a = {
    "name" : "Umar",
    "from" : "India",
    "marks" : [92,93,94]
    }

print(a.items()) #Returns (key,value) tuples
print(a.keys()) #List of keys
a.update({"friends":0}) #To add
print(a.get("name"))