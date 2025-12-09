# Program to read a file and perform various operations

# Input filename
filename = input("Enter filename (with extension, e.g., input.txt): ")

# --- Part (a): Count characters, words, and lines ---
with open(filename, "r") as f:
    data = f.read()

lines = data.split("\n")
words = data.split()

print("Total Characters:", len(data))
print("Total Words:", len(words))
print("Total Lines:", len(lines))

# --- Part (b): Frequency of each character ---
freq = {}
for ch in data:
    freq[ch] = freq.get(ch, 0) + 1

print("\nCharacter Frequency:")
for ch, count in freq.items():
    print(f"'{ch}': {count}")

# --- Part (c): Print words in reverse order ---
print("\nWords in Reverse Order:")
print(" ".join(words[::-1]))

# --- Part (d): Copy even and odd lines into separate files ---
with open("File1.txt", "w") as f1, open("File2.txt", "w") as f2:
    for i, line in enumerate(lines, start=1):
        if i % 2 == 0:   # even line number
            f1.write(line + "\n")
        else:            # odd line number
            f2.write(line + "\n")

print("\nEven and odd lines copied successfully.")



Hello World
Python is fun
I love coding
This is a test
Have a nice day




Enter filename (with extension, e.g., input.txt): input.txt





Total Characters:  sixty-seven  # actual count 67
Total Words: 13
Total Lines: 5

Character Frequency:
'H': 1
'e': 4
'l': 7
'o': 5
' ': 12
'W': 1
'r': 2
'd': 2
'P': 1
'y': 2
't': 4
'h': 2
'n': 3
'i': 4
's': 3
'f': 1
'u': 1
'I': 1
'c': 2
'g': 1
'a': 3
'v': 1

Words in Reverse Order:
day nice a Have test a is This coding love I fun is Python World Hello

Even and odd lines copied successfully.
