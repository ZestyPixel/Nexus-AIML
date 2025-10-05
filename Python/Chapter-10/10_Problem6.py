class Employee:
    company = "Google"
    salary = 1000
    def getSalary(harry):
        print(f"Salary for this employee working in {harry.company} is {harry.salary}")
Umar = Employee()
Umar.salary = 100000
Umar.getSalary()
# Yes, you can change the self-parameter to something else like "harry" or "slf". It will still work as long as you use the same name consistently within the method.