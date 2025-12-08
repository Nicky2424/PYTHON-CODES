
# ----------- 1) CHECK IF A NUMBER IS PRIME -----------

n = int(input("Enter a number to check if it is prime: "))

if n <= 1:
    print(n, "is NOT a prime number")
else:
    is_prime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print(n, "is a prime number")
    else:
        print(n, "is NOT a prime number")


# ----------- 2) PRINT ALL PRIME NUMBERS UP TO n -----------

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

print("\nPrime numbers up to", n, ":")
for num in range(2, n + 1):
    if is_prime(num):
        print(num, end=" ")

print("\n")


# ----------- 3) PRINT FIRST n PRIME NUMBERS -----------

def print_first_n_primes(count):
    print("First", count, "prime numbers:")
    num = 2
    primes_found = 0

    while primes_found < count:
        if is_prime(num):
            print(num, end=" ")
            primes_found += 1
        num += 1

print_first_n_primes(n)
