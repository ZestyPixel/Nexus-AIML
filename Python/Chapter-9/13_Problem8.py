path = r"C:\Users\umar2\Desktop\Coding\Nexus-AIML\Python\Chapter-9\this.txt"

with open(path) as f:
    content = f.read()

with open(r"C:\Users\umar2\Desktop\Coding\Nexus-AIML\Python\Chapter-9\this_copy.txt", "w") as f:
    f.write(content)