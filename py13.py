name = input("Enter your name: ")

try:
    if not name.isalpha():
        raise ValueError("Name contains digits or special characters")
    else:
        print("Valid name:", name)

except ValueError as e:
    print("Error:", e)
