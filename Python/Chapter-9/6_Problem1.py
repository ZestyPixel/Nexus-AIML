f = open(r"C:\Users\umar2\Desktop\Coding\Nexus-AIML\Python\Chapter-9\poem.txt",'r')
content = f.read()
if("twinkle" in content):
    print("The word twinkle is present in the content")

else:
    print("The word twinkle is not present in the content")

f.close()