# Get the first string
a = input("Enter the first string: ")
print()

# Get the second string
b = input("Enter the second string: ")
print()

# Get the number of characters to swap
n = int(input("Enter the number of characters to swap: "))

# Swap the first n characters
new_a = b[:n] + a[n:]
new_b = a[:n] + b[n:]

# Print the new strings
print("The new strings after swapping the first", n, "characters are:")
print("First string:", new_a)
print("Second string:", new_b)
