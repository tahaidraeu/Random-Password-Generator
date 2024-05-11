 import random
import string

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    characters = ''
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "Error: No character set selected."

    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("Random Password Generator")
    while True:
        try:
            num_passwords = int(input("Enter the number of passwords to generate: "))
            if num_passwords <= 0:
                print("Please enter a number greater than 0.")
                continue
            length = int(input("Enter the length of each password (at least 6 characters): "))
            if length < 6:
                print("Password length should be at least 6 characters.")
                continue
            use_upper = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
            use_lower = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
            use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
            use_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'

            for _ in range(num_passwords):
                password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
                print("Your random password:", password)
            
            break
        except ValueError:
            print("Please enter valid numbers.")

if __name__ == "__main__":
    main()
