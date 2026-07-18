password = input("Enter your password: ")

has_upper = False
has_lower = False
has_number = False
has_special = False


for character in password:

    if character.isupper():
        has_upper = True

    elif character.islower():
        has_lower = True

    elif character.isdigit():
        has_number = True

    else:
        has_special = True


score = 0


if len(password) >= 8:
    score += 1

if has_upper:
    score += 1

if has_lower:
    score += 1

if has_number:
    score += 1

if has_special:
    score += 1


print("\nPassword Report")
print("----------------")

print("Length:", len(password))
print("Strength score:", score, "/ 5")


if score <= 2:
    print("Strength: Weak")

elif score <= 4:
    print("Strength: Medium")

else:
    print("Strength: Strong")