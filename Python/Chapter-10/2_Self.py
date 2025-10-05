class Employee:
    company = "Google"
    salary = 1000
    def getSalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary}")

Umar = Employee()
Umar.salary = 100000
Umar.getSalary()