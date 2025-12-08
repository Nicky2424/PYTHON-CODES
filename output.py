# ============================================
# 1. Roots of Quadratic Equation
# ============================================

import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

disc = b*b - 4*a*c

if disc > 0:
    r1 = (-b + math.sqrt(disc)) / (2*a)
    r2 = (-b - math.sqrt(disc)) / (2*a)
    print("Roots:", r1, r2)
elif disc == 0:
    r = -b / (2*a)
    print("Equal roots:", r)
else:
    print("Imaginary roots")

# Sample Output:
# Enter a: 1
# Enter b: 5
# Enter c: 6
# Roots: -2.0 -3.0


# ============================================
# 2. Prime number operations
# ============================================

def is_prime(n):
    if n <= 1: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

n = int(input("Enter n: "))

# a. Check prime
print("Prime?", is_prime(n))

# b. All primes till n
print("Primes till n:", [i for i in range(2, n+1) if is_prime(i)])

# c. First n primes
primes = []
x = 2
while len(primes) < n:
    if is_prime(x): primes.append(x)
    x += 1
print("First n primes:", primes)

# Sample Output:
# Enter n: 10
# Prime? False
# Primes till n: [2,3,5,7]
# First n primes: [2,3,5,7,11,13,17,19,23,29]


# ============================================
# 3. Pyramid and Reverse Pyramid
# ============================================

rows = int(input("Rows: "))
for i in range(1, rows+1):
    print("*" * i)

for i in range(rows, 0, -1):
    print("*" * i)

# Sample Output for rows=3:
# *
# **
# ***
# ***
# **
# *


# ============================================
# 4. Character Check
# ============================================

ch = input("Enter a character: ")

if ch.isalpha():
    print("Letter")
    print("Uppercase" if ch.isupper() else "Lowercase")
elif ch.isdigit():
    print("Digit")
    names = ["ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"]
    print(names[int(ch)])
else:
    print("Special Character")

# Output Example:
# Enter a: G
# Letter
# Uppercase


# ============================================
# 5. String Operations
# ============================================

s = input("String: ")
ch = input("Character: ")
new = input("Replace with: ")

# a. Frequency
print("Frequency:", s.count(ch))

# b. Replace
print("Replaced:", s.replace(ch, new))

# c. Remove first occurrence
print("Remove first:", s.replace(ch, "", 1))

# d. Remove all
print("Remove all:", s.replace(ch, ""))

# Output Sample:
# String: banana
# Character: a
# Replace with: o
# Frequency: 3
# Replaced: bonono
# Remove first: bnana
# Remove all: bnn


# ============================================
# 6. Swap first n characters of 2 strings
# ============================================

s1 = input("First string: ")
s2 = input("Second string: ")
n = int(input("n: "))

s1_new = s2[:n] + s1[n:]
s2_new = s1[:n] + s2[n:]

print("After swap:", s1_new, s2_new)

# Output:
# First string: hello
# Second string: world
# n: 2
# After swap: wollo herld


# ============================================
# 7. Return all indices of substring
# ============================================

def find_indices(s1, s2):
    idx = []
    start = 0
    while True:
        pos = s1.find(s2, start)
        if pos == -1: break
        idx.append(pos)
        start = pos + 1
    return idx if idx else -1

print(find_indices(input("String: "), input("Search: ")))

# Output:
# String: banana
# Search: an
# [1, 3]


# ============================================
# 8. List of cubes of even integers
# ============================================

lst = eval(input("List: "))

# a. using for loop
ev = []
for i in lst:
    if type(i) == int and i % 2 == 0:
        ev.append(i**3)
print("For loop:", ev)

# b. list comprehension
print("List comp:", [i**3 for i in lst if type(i)==int and i%2==0])

# Output:
# List: [1,2,3,4,5,'a']
# For loop: [8,64]
# List comp: [8,64]


# ============================================
# 9. File Handling
# ============================================

fname = input("Filename: ")
f = open(fname, "r")
data = f.read()
f.seek(0)
lines = f.readlines()
f.close()

# a. Count
print("Characters:", len(data))
print("Words:", len(data.split()))
print("Lines:", len(lines))

# b. Frequency of each character
freq = {}
for ch in data:
    freq[ch] = freq.get(ch, 0) + 1
print("Frequency:", freq)

# c. Words in reverse
print("Reverse words:", " ".join(data.split()[::-1]))

# d. Even/odd lines
open("File1.txt", "w").writelines(lines[1::2])  # even lines
open("File2.txt", "w").writelines(lines[0::2])  # odd lines

# Output:
# Characters: 20
# Words: 4
# Lines: 2
# File1 and File2 created


# ============================================
# 10. Class Point + Distance
# ============================================

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"
    def distance(self, other):
        return math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2)

p1 = Point(3, 4)
p2 = Point(6, 8)
print("Points:", p1, p2)
print("Distance:", p1.distance(p2))

# Output:
# Points: (3,4) (6,8)
# Distance: 5.0


# ============================================
# 11. Dictionary of cubes
# ============================================

print({x: x**3 for x in range(1, 6)})

# Output:
# {1:1, 2:8, 3:27, 4:64, 5:125}


# ============================================
# 12. Tuple operations
# ============================================

t1 = (1,2,5,7,9,2,4,6,8,10)

# a. Half values
print(t1[:len(t1)//2])
print(t1[len(t1)//2:])

# b. Even tuple
print(tuple(i for i in t1 if i%2==0))

# c. Concatenate
t2 = (11,13,15)
print(t1 + t2)

# d. Max & Min
print(max(t1), min(t1))

# Output:
# (1,2,5,7,9)
# (2,4,6,8,10)
# (2,2,4,6,8,10)
# (1,2,5,7,9,2,4,6,8,10,11,13,15)
# 15 1


# ============================================
# 13. Exception handling for name
# ============================================

name = input("Enter name: ")

try:
    if not name.isalpha():
        raise ValueError("Invalid name")
    print("Valid Name")
except ValueError as e:
    print(e)

# Output:
# Enter name: Nandani
# Valid Name
