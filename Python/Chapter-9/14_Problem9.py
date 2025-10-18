with open(r"C:\Users\umar2\Desktop\Coding\Nexus-AIML\Python\Chapter-9\this.txt") as f:
    content1 = f.read()

with open(r"C:\Users\umar2\Desktop\Coding\Nexus-AIML\Python\Chapter-9\this_copy.txt") as f:
    content2 = f.read()

if(content1 == content2):
    print("Yes these files are identical")

else: 
    print("No these files are not identical")