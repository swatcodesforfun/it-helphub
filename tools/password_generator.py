import random
import string


print("""
==========================
 IT HelpHub Password Generator
==========================
""")


length = int(input("Password length: "))


characters = ""


uppercase = input("Include uppercase letters? (y/n): ")
numbers = input("Include numbers? (y/n): ")
symbols = input("Include symbols? (y/n): ")


if uppercase == "y":
    characters += string.ascii_uppercase


if numbers == "y":
    characters += string.digits


if symbols == "y":
    characters += "!@#$%^&*"


if characters == "":
    print("You must select at least one character option.")
    exit()


password = ""


for i in range(length):

    random_character = random.choice(characters)

    password += random_character


print("""
==========================
 Generated Password
==========================
""")

print(password)