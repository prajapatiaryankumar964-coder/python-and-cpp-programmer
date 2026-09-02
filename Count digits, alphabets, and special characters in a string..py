text = input("Enter string: ")
alpha = digit = special = 0

for char in text:
    if char.isalpha():
        alpha += 1
    elif char.isdigit():
        digit += 1
    elif not char.isspace():
        special += 1

print(f"Alphabets: {alpha}\nDigits: {digit}\nSpecial Characters: {special}")