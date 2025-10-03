favorite_languages = {}  # empty dictionary

print("Enter the names of 4 friends and their favorite programming languages:")

for i in range(4):
    name = input(f"Friend {i+1} name: ").strip()
    language = input(f"{name}'s favorite language: ").strip()
    favorite_languages[name] = language

print("\nFavorite languages of friends:")

for friend, lang in favorite_languages.items():
    print(f"{friend} : {lang}")

# The previous value gets overwritten if the name of two friends is the same