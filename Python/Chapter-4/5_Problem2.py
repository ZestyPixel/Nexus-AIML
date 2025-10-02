students = []
for i in range (6):
    marks = int(input("Enter marks: "))
    students.append(marks)

students.sort()

for i in range(len(students)):
    print(students[i])

