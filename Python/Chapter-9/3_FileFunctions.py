file = open(r'C:\Users\umar2\Desktop\Coding\Nexus-AIML\Python\Chapter-9\file.txt')
data = file.readlines()
print(data) # Reads all lines and returns them as a list.

# data2= file.readline() Reads only one line at a time
file.close()