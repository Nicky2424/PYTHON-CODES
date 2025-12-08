n = int(input("enter a number to check for prime or not"))
if n <= 1:
    print("not prime")
else:
    is_prime = True  # Flag variable
    for i in range(2, n + 1):
        if n % i == 0:
            is_prime = False
            
            print("not a prime no")
            break
        else:
            print("yes a prime no ")
            break

def is_prime(num):
   if num <= 1:
       return False
   for i in range(2, int(num**0.5) + 1):
       if num % i == 0:
           return False
   return True
def print_primes(n):
   for num in range(2, n + 1):
       if is_prime(num):
           print(num)

print_primes(n)

def print_prim(n):
   if n < 2:
       print("No prime numbers available.")
       return
   # Create a boolean array to mark prime numbers
   primes = [True] * (n + 1)
   primes[0] = primes[1] = False # 0 and 1 are not prime numbers
   # Mark non-prime numbers
   for i in range(2, int(n**0.5) + 1):
       if primes[i]:
           for j in range(i * i, n + 1, i):
               primes[j] = False
   # Print all prime numbers
   for i in range(2, n + 1):
       if primes[i]:
           print(i, end=" ")

print_prim(n)
