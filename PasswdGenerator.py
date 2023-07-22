import random
import string

def generate_password(length, use_special_characters=True, use_numbers=True, use_uppercase_letters=True,
                      use_lowercase_letters=True, avoid_repetitions=True):
    characters = ''
    
    if use_special_characters:
        characters += string.punctuation
    if use_numbers:
        characters += string.digits
    if use_uppercase_letters:
        characters += string.ascii_uppercase
    if use_lowercase_letters:
        characters += string.ascii_lowercase
    
    password = [random.choice(characters) for _ in range(length)]
    
    if avoid_repetitions:
        while any(password[i] == password[i+1] for i in range(len(password) - 1)):
            password = [random.choice(characters) for _ in range(length)]
    
    return ''.join(password)

def check_requirements(password, use_special_characters, use_numbers, use_uppercase_letters, use_lowercase_letters):
    has_special_characters = any(c in string.punctuation for c in password)
    has_numbers = any(c in string.digits for c in password)
    has_uppercase_letters = any(c in string.ascii_uppercase for c in password)
    has_lowercase_letters = any(c in string.ascii_lowercase for c in password)
    
    return (not use_special_characters or has_special_characters) and \
           (not use_numbers or has_numbers) and \
           (not use_uppercase_letters or has_uppercase_letters) and \
           (not use_lowercase_letters or has_lowercase_letters)

def calculate_password_strength(password):
    points = 0
    password_length = len(password)
    
    points += max(0, min(2, password_length // 8))  # Points for minimum password length
    points += min(2, len(set(password)) // 2)  # Points for character diversity
    points += min(2, sum(c in string.punctuation for c in password))  # Points for special characters
    points += min(2, sum(c in string.digits for c in password))  # Points for numbers
    points += min(2, sum(c in string.ascii_uppercase for c in password))  # Points for uppercase letters
    points += min(2, sum(c in string.ascii_lowercase for c in password))  # Points for lowercase letters
    
    # Check for character sequences (e.g., abc, 123)
    for seq in [string.ascii_lowercase, string.ascii_uppercase, string.digits]:
        if seq in password or seq[::-1] in password:
            points -= 2
    
    # Check for repeated character sequences (e.g., aa, 111)
    for c in set(password):
        if password.count(c) >= 3:
            points -= 1
    
    return points

def main():
    while True:
        try:
            num_passwords = int(input("How many passwords do you want: "))
            password_length = int(input("Enter the number of characters for each password: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        use_special_characters = input("Use special characters? (y/n): ").lower() == 'y'
        use_numbers = input("Use numbers? (y/n): ").lower() == 'y'
        use_uppercase_letters = input("Use uppercase letters? (y/n): ").lower() == 'y'
        use_lowercase_letters = input("Use lowercase letters? (y/n): ").lower() == 'y'
        avoid_repetitions = input("Avoid repeated characters? (y/n): ").lower() == 'y'

        passwords = []
        while len(passwords) < num_passwords:
            password = generate_password(password_length, use_special_characters, use_numbers,
                                         use_uppercase_letters, use_lowercase_letters, avoid_repetitions)
            if check_requirements(password, use_special_characters, use_numbers,
                                  use_uppercase_letters, use_lowercase_letters):
                passwords.append(password)

        print(f"{num_passwords} passwords generated:")

        for password in passwords:
            print(password)
            strength = calculate_password_strength(password)
            print(f"Password strength: {strength} point(s).\n")

        option = input("Do you want to generate more passwords? (y/n): ").lower()
        if option != "y":
            break

if __name__ == "__main__":
    main()
