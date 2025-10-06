import random
n = random.randint(1, 100)
a = -1
guesses = 1
while (a!=n):
    a = int(input("Enter your guess:"))
    if(a<n):
        print("Go higher")
        guesses +=1
    elif(a>n):
        print("Go lower")
        guesses +=1

print(f"You have guessed the correct number {n} in {guesses} guesses.")