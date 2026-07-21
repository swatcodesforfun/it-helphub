import random
import string


def generate_password(length, uppercase, numbers, symbols):

    characters = string.ascii_lowercase

    if uppercase:
        characters += string.ascii_uppercase

    if numbers:
        characters += string.digits

    if symbols:
        characters += "!@#$%^&*"

    password = ""

    for i in range(length):

        password += random.choice(characters)

    return password