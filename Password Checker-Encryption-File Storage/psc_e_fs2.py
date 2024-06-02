##################################################
####
####
####  Password Strength Checker/ Encryption / File Storage
####                   By Rhyan
####
####
##################################################

#provides regular expression support
import re
import random
import string
import pyperclip #imported to add to clipboard
import os

#static variable
directory = os.path.dirname(os.path.abspath(__file__))
file_name = "encrypted_password.txt"
file_path = os.path.join(directory, file_name)

def check_password_strength(password):
    # Check for uppercase and lowercase letters
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    # If password meets 3 out of 4 criteria
    criteria_met = sum([
        len(password) >= 8,
        (has_uppercase and has_lowercase),
        #has_uppercase,
        #has_lowercase,
        any(char.isdigit() for char in password),
        bool(re.search(r"[!@#$%^&*()_+{}|:<>?~-]", password))
    ])
    
    #Checking criteria
    if criteria_met == 4:  # Adjusted to 4 to ensure
        return "Strong"
    elif criteria_met == 3:
        return "Medium"
    else:
        return "Weak"

def crypto(str_text, s):
    result = ""

    for char in str_text:
        ascii_val = ord(char)
        if 32 <= ascii_val <= 126:
            # Shift within the ASCII printable characters range
            shifted_val = 32 + (ascii_val - 32 + s) % 95
            result += chr(shifted_val)
        else:
            # Leave the character unchanged if it is outside the range
            result += char

    return result

def generate_password(length):
    #defining characters
    upperLet = string.ascii_uppercase
    lowerLet = string.ascii_lowercase
    digits = string.digits
    specialChar = string.punctuation
    #combining all the characters together
    combinedPass = upperLet + lowerLet + digits + specialChar

    Password = ''.join(random.choice(combinedPass) for _ in range(length)) #the ' ' classifies this as a string
    return Password

while True:
    try:
        # Ask how long the password
        length_str = input("Enter the length of the password: ")
        length = int(length_str)
        
        if length <= 0:
            print("Please enter a positive integer greater than 0.")
        else:
            # Generate password
            password = generate_password(length)
            
            print("Generated Password:", password)
            check = check_password_strength(password)
            print(f"Password strength: {check}")
            pyperclip.copy(password)
            print("Password copied to clipboard!")
            break  # Exit the loop after generating a valid password
    
    except ValueError:
        print("Invalid input. Please enter a valid integer for the password length.")
    
# picking random shift variable  
shift = random.randint(32,126)

encrypt = crypto(password, shift)
print("password: " +password)
print("encrypted password: "  +encrypt)

data_append = encrypt
# chose append so any other data in file is not overwriten.
# with open is best practice as it automatically closes the file
with open(file_path, 'a') as file:
    file.write(str(data_append) + '\n')