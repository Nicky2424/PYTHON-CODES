# Get the input string
string = input("Enter the string: ")

# Part a: Find the frequency of a character in the string
char_to_count = input("Enter the character to find frequency of: ")
frequency = string.count(char_to_count)
print(f"Frequency of '{char_to_count}' in the string: {frequency}")

# Part b: Replace a character by another character in the string
old_char = input("Enter the character to replace: ")
new_char = input("Enter the new character: ")
replaced_string = string.replace(old_char, new_char)
print(f"String after replacement: {replaced_string}")

# Part c: Remove the first occurrence of a character from the string
char_to_remove_first = input("Enter the character to remove first occurrence of: ")
index = string.find(char_to_remove_first)
if index != -1:
    string_after_remove_first = string[:index] + string[index + 1:]
else:
    string_after_remove_first = string
print(f"String after removing first occurrence of '{char_to_remove_first}': {string_after_remove_first}")

# Part d: Remove all occurrences of a character from the string
char_to_remove_all = input("Enter the character to remove all occurrences of: ")
string_after_remove_all = string.replace(char_to_remove_all, '')
print(f"String after removing all occurrences of '{char_to_remove_all}': {string_after_remove_all}")
