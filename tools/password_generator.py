import random
import string


print("""
==========================
 IT HelpHub Password Generator
==========================
""")


length = int(input("How long should the password be? "))


characters = string.ascii_letters + string.digits + "!@#$%^&*"


password = ""


for i in range(length):

    random_character = random.choice(characters)

    password += random_character


print("\nGenerated Password:")
print(password)