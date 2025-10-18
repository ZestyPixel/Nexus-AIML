path = r"C:\Users\umar2\Desktop\Coding\Nexus-AIML\Python\Chapter-9\log.txt"

with open(path) as f:
    content = f.read()

if("python" in content):
    print("Yes python is present")
else:
    print("No Python is not present")