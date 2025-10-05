class MyClass:
    a = 10

obj = MyClass()
print("Before:", MyClass.a)
obj.a = 0
print("After:", MyClass.a)  
print("Object a:", obj.a)

#This is because when we do obj.a = 0, it creates an instance variable a for the object obj, 
# which shadows the class variable a. The class variable MyClass.a remains unchanged.
