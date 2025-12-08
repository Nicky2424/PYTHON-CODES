# -------- 1) CHECK IF A NUMBER IS PRIME --------

def check_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Enter a number: "))

if check_prime(n):
    print(n, "is a prime number")
else:
    print(n, "is NOT a prime number")


# -------- 2) PRINT ALL PRIME NUMBERS UP TO n --------

print("\nPrime numbers up to", n, ":")

for num in range(2, n + 1):
    if check_prime(num):
        print(num, end=" ")

print("\n")


# -------- 3) PRINT FIRST n PRIME NUMBERS --------

print("First", n, "prime numbers:")

count = 0
num = 2

while count < n:
    if check_prime(num):
        print(num, end=" ")
        count += 1
    num += 1

