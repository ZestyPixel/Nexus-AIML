#Single Inheritance
class Parent:
    def func1(self):
        print("This function is in parent class.")

class Child(Parent):
    def func2(self):
        print("This function is in child class.")

object = Child()
object.func1()
object.func2()
print("\n")

#Multiple Inheritance
class Mother:
    def func1(self):
        print("This function is in mother class.")
class Father:

    def func2(self):
        print("This function is in father class.")

class Child(Mother, Father):
    def func3(self):
        print("This function is in child class.")

object = Child()
object.func1()
object.func2()
object.func3()
print("\n")

#Multilevel Inheritance
class Grandfather:
    def func1(self):
        print("This function is in grandfather class.")

class Father(Grandfather):
    def func2(self):
        print("This function is in father class.")

class Child(Father):
    def func3(self):
        print("This function is in child class.")

object = Child()
object.func1()
object.func2()
object.func3()
print("\n")

#Hierarchical Inheritance
class Parent:
    def func1(self):
        print("This function is in parent class.")

class Child1(Parent):
    def func2(self):
        print("This function is in child 1 class.")

class Child2(Parent):
    def func3(self):
        print("This function is in child 2 class.")

object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()

#Hybrid Inheritance- Mix of different types of inheritance