char = input("Enter a single character: ")

# Check length
if len(char) != 1:
    print("Please enter only one character.")
else:
    # Dictionary for digit names
    digit_names = {
        '0': "zero", '1': "one", '2': "two", '3': "three", '4': "four",
        '5': "five", '6': "six", '7': "seven", '8': "eight", '9': "nine"
    }

    if char.isdigit():
        print("Numeric Digit")
        print("In text:", digit_names[char])

    elif char.isalpha():
        print("Letter")
        if char.isupper():
            print("Uppercase")
        else:
            print("Lowercase")

    else:
        print("Special Character")

