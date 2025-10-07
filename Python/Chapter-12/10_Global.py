a = 5
b = 10

def func():
    a = 1
    global b 
    b = 2
    print(a)
    print(b)

print(a) #This prints the global variable a
print(b) #This prints the global variable b = 10
func() # In function a = 1 and b = 2
