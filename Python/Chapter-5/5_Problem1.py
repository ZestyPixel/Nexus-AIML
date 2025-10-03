words = {
    "Joota" : "Shoe",
    "Botal" : "Bottle"
}

word = input("Enter a word in Hindi: ")

print("The meaning of your word is:", words.get(word, "Not found"))