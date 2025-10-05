class Programmer:
    def __init__(self, name, age, salary, language):
        self.name = name
        self.age = age
        self.salary = salary
        self.language = language

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Language: {self.language}")

p1 = Programmer("Umar", 25, 50000, "Python")
p2 = Programmer("Alice", 30, 60000, "Java")
p3 = Programmer("Bob", 28, 55000, "C++")
p1.display()
p2.display()

