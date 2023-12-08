import random
import string

def generate_password(length, complexity):
    # Define character sets based on complexity
    if complexity == "1":
        characters = string.ascii_letters
    elif complexity == "2":
        characters = string.ascii_letters + string.digits
    elif complexity == "3":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        print("Invalid complexity level. Please choose from Weak, Medium, or Strong.")
        return None

    # Generate a random password using specified length and character set
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

while True:
    try:
        password_length = int(input("\nEnter the desired length for the password: "))
        break
    except ValueError:
        print("Please enter a valid integer for the password length.")

# Prompt the user for password complexity
while True:
    print("1.Weak password")
    print("2.Medium password")
    print("3.Strong password")
    complexity = input("Enter the desired complexity: ")

    if complexity in ["1", "2", "3"]:
        break
    else:
        print("Invalid complexity level. Please choose from Weak, Medium, or Strong.")

# Generate and display the password
password = generate_password(password_length, complexity)
if password:
    print("Generated Password: ", password)
else:
    print("Please enter a password length greater than 0.")
print()