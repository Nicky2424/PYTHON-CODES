# Get input string
string = input("Enter the string: ")

# a) Find frequency of a character
char1 = input("Enter character to find frequency: ")
print(f"Frequency of '{char1}':", string.count(char1))

# b) Replace a character by another character
old = input("Enter character to replace: ")
new = input("Enter new character: ")
print("After replacement:", string.replace(old, new))

# c) Remove first occurrence of a character
char2 = input("Enter character to remove first occurrence: ")
idx = string.find(char2)
if idx != -1:
    print("After removing first occurrence:", string[:idx] + string[idx+1:])
else:
    print("Character not found")

# d) Remove all occurrences of a character
char3 = input("Enter character to remove all occurrences: ")
print("After removing all occurrences:", string.replace(char3, ""))










