a = int(input("Enter marks of first subject: "))
b = int(input("Enter marks of second subject: "))   
c = int(input("Enter marks of third subject: "))

if(a<33 or b<33 or c<33):
    print("You have failed")
elif((a+b+c)/3 < 40):
    print("You have failed")
else:
    print("You have passed")