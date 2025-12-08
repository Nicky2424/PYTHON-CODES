# Accept a character from the user
char = input("Enter a single character: ")

# Check if the input is a single character
if len(char) != 1:
    print("Please enter only one character.")
else:
    # Check if the character is a digit
    if char.isdigit():
        print(f"'{char}' is a numeric digit.")
    # Check if the character is an alphabet
    elif char.isalpha():
        if char.islower():
            print(f"'{char}' is a lowercase letter.")
        else:
            print(f"'{char}' is an uppercase letter.")
    # If neither digit nor alphabet, it is a special character
    else:
        print(f"'{char}' is a special character.")
