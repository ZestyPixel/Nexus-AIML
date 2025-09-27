import os

directory_path = 'C:/Users/umar2/Desktop/Coding/Nexus-AIML/Python/Chapter-1'

contents = os.listdir(directory_path)

for item in contents:
    print(item)