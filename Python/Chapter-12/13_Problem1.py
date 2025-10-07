try: 
    with (
        open("f1.txt", "r") as f1,
        open("f2.txt", "r") as f2,
        open("f3.txt", "r") as f3
    ): 
        pass
except Exception as e:
    print("One of the files was not found.")
    print(e)
