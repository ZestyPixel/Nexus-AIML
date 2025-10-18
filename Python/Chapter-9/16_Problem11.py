with open(r"C:\Users\umar2\Desktop\Coding\Nexus-AIML\Python\Chapter-9\old.txt") as f:
    content = f.read()

with open(r"C:\Users\umar2\Desktop\Coding\Nexus-AIML\Python\Chapter-9\renamed_by_python.txt", "w") as f:
    f.write(content)