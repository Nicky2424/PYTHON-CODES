# -----------------------------------------------------------
# 1. Write a program to find the roots of a quadratic equation
# -----------------------------------------------------------
import math
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
d = b*b - 4*a*c
if d >= 0:
    r1 = (-b + math.sqrt(d)) / (2*a)
    r2 = (-b - math.sqrt(d)) / (2*a)
    print("Roots:", r1, r2)
else:
    print("Imaginary roots")

# --------------------------------------------------------------------
# 2. Prime number functions: check prime, primes till n, first n primes
# --------------------------------------------------------------------
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

n = int(input("Enter n: "))

print("Prime?", is_prime(n))

print("Primes till n:", [i for i in range(2, n+1) if is_prime(i)])

primes = []
x = 2
while len(primes) < n:
    if is_prime(x): primes.append(x)
    x += 1
print("First n primes:", primes)

# -----------------------------------------
# 3. Pyramid and Reverse Pyramid using '*'
# -----------------------------------------
rows = int(input("Rows: "))
for i in range(1, rows+1): print("*"*i)
for i in range(rows, 0, -1): print("*"*i)

# ----------------------------------------------------------------------
# 4. Character type: letter/digit/special + case + digit name in words
# ----------------------------------------------------------------------
ch = input("Enter a character: ")
if ch.isalpha():
    print("Letter")
    print("Uppercase" if ch.isupper() else "Lowercase")
elif ch.isdigit():
    print("Digit")
    names = ["ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"]
    print(names[int(ch)])
else:
    print("Special character")

# -----------------------------------------------------------
# 5. String operations: frequency, replace, remove 1st, remove all
# -----------------------------------------------------------
s = input("String: ")
ch = input("Char for frequency: ")
print("Frequency:", s.count(ch))

old = input("Char to replace: ")
new = input("Replace with: ")
print("After replace:", s.replace(old, new))

rem = input("Char to remove first: ")
print("After removing first:", s.replace(rem, "", 1))

rem2 = input("Char remove all: ")
print("After removing all:", s.replace(rem2, ""))

# ---------------------------------------------
# 6. Swap first n characters of two strings
# ---------------------------------------------
s1 = input("String 1: ")
s2 = input("String 2: ")
n = int(input("n: "))
s1_new = s2[:n] + s1[n:]
s2_new = s1[:n] + s2[n:]
print(s1_new, s2_new)

# ------------------------------------------------------------------------
# 7. Function: return indices of all occurrences of substring, else -1
# ------------------------------------------------------------------------
def find_occurrences(s1, s2):
    idx = []
    pos = s1.find(s2)
    while pos != -1:
        idx.append(pos)
        pos = s1.find(s2, pos+1)
    return idx if idx else -1

print(find_occurrences(input("String 1: "), input("String 2: ")))

# -------------------------------------------------------------------
# 8. Create list of cubes of even integers (for loop + list comp)
# -------------------------------------------------------------------
lst = [10, "hi", 3, 8, 2, 5.6, 4]
even_cubes_loop = []
for x in lst:
    if type(x) == int and x % 2 == 0:
        even_cubes_loop.append(x**3)
print("For loop:", even_cubes_loop)

even_cubes_lc = [x**3 for x in lst if type(x)==int and x%2==0]
print("List comp:", even_cubes_lc)

# --------------------------------------------------------------
# 9. File Handling operations
# --------------------------------------------------------------
f = open("input.txt","r")
data = f.read()
f.close()

print("Characters:", len(data))
words = data.split()
print("Words:", len(words))
lines = data.split("\n")
print("Lines:", len(lines))

freq = {}
for ch in data:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)

print("Words reversed:", words[::-1])

f1 = open("File1.txt","w")
f2 = open("File2.txt","w")
for i, line in enumerate(lines, start=1):
    if i % 2 == 0: f1.write(line+"\n")
    else: f2.write(line+"\n")
f1.close()
f2.close()

# ------------------------------------------------------
# 10. Class Point + distance between two point objects
# ------------------------------------------------------
import math
class Point:
    def __init__(self, x, y):
        self.x = x; self.y = y
    def distance(self, other):
        return math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2)
    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Point(float(input()), float(input()))
p2 = Point(float(input()), float(input()))
print("Distance:", p1.distance(p2))

# -------------------------------------------------------------
# 11. Dictionary of numbers 1 to 5 with cubes as values
# -------------------------------------------------------------
cube_dict = {x: x**3 for x in range(1,6)}
print(cube_dict)

# ----------------------------------------------------------------------
# 12. Tuple operations
# ----------------------------------------------------------------------
t1 = (1,2,5,7,9,2,4,6,8,10)
mid = len(t1)//2
print(t1[:mid])
print(t1[mid:])

evens = tuple(x for x in t1 if x%2==0)
print("Even tuple:", evens)

t2 = (11,13,15)
print("Concatenated:", t1 + t2)

print("Max:", max(t1))
print("Min:", min(t1))

# --------------------------------------------------------------
# 13. Accept name; raise exception if digits/special characters
# --------------------------------------------------------------
name = input("Enter name: ")
try:
    if not name.isalpha():
        raise ValueError("Invalid name: contains digits/special chars")
    print("Valid name")
except ValueError as e:
    print(e)
