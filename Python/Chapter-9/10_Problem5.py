words = ["Donkey", "bad", "ganda"]

path = r"C:\Users\umar2\Desktop\Coding\Nexus-AIML\Python\Chapter-9\file.txt"

with open(path, "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))

with open(path, "w") as f:
    f.write(content)
