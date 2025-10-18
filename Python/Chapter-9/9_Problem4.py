word = "Donkey"

path = r"C:\Users\umar2\Desktop\Coding\Nexus-AIML\Python\Chapter-9\file3.txt"

with open(path, 'r') as f:
    content = f.read()

contentNew = content.replace(word, "######")

with open(path, "w") as f:
    f.write(contentNew)
